/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


import org.apache.giraph.Algorithm;
import org.apache.giraph.conf.GiraphConfiguration;
import org.apache.giraph.edge.Edge;
import org.apache.giraph.edge.MutableEdge;
import org.apache.giraph.graph.BasicComputation;
import org.apache.giraph.graph.Vertex;
import org.apache.giraph.io.formats.GiraphFileInputFormat;
import org.apache.giraph.io.formats.GiraphTextOutputFormat;
import org.apache.giraph.job.GiraphJob;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

/**
 * Demonstrates the basic Pregel shortest paths implementation.
 */
@Algorithm(
        name = "Shortest paths",
        description = "Finds all shortest paths from a selected vertex"
)
public  class Find_triangle extends BasicComputation<
        LongWritable, Text, IntWritable, Message>  implements Tool {

    private boolean ordering(int degreeA, long idA, int degreeB, long idB) {
        if(degreeA < degreeB) {
            return true;
        }
        if(degreeA == degreeB) {
            if(idA < idB) {
                return true;
            }
        }
        return false;
    }

    @Override
    public void compute(Vertex<LongWritable, Text, IntWritable> vertex, Iterable<Message> messages) throws IOException {

        // Phase 0 - compute degrees and send them out

        if(getSuperstep() == 0) {

            IntWritable degree = new IntWritable(vertex.getNumEdges());
            vertex.setValue(new Text(degree.toString()));
            sendMessageToAllEdges(vertex, new Message(vertex.getId(), degree));
        }

        // Phase 1 - annotate degrees onto edges
        if(getSuperstep() == 1) {
            for(Message message : messages) {
                vertex.setEdgeValue(message.getSource(), new IntWritable(message.getDegree().get()));
                //System.out.println("+++++++++++++++++++++"+message.toString()+"+++++++++++++++++++++");
            }
        }

        // Phase 2 - Query neighbours about possible triangles
        if(getSuperstep() == 2) {
            int myDegree = Integer.parseInt(vertex.getValue().toString());
            if(myDegree > 1) {
                for(Edge<LongWritable, IntWritable> neighbourA : vertex.getEdges()) {
                    int neighbourADegree = (int)neighbourA.getValue().get();
                    if(ordering(myDegree, vertex.getId().get(), neighbourADegree, neighbourA.getTargetVertexId().get())) {
                        for(Edge<LongWritable, IntWritable> neighbourB : vertex.getEdges()) {
                            int neighbourBDegree = (int)neighbourB.getValue().get();
                            if(ordering(neighbourADegree, neighbourA.getTargetVertexId().get(), neighbourBDegree, neighbourB.getTargetVertexId().get())) {
                                System.out.println("I am node " + vertex.getId() + ", and I will ask node " + neighbourA.getTargetVertexId() + " whether it links to  " + neighbourB.getTargetVertexId());
                                sendMessage(neighbourA.getTargetVertexId(), new Message(vertex.getId(), neighbourB.getTargetVertexId()));
                            }
                        }
                    }
                }
            }
            for(MutableEdge<LongWritable, IntWritable> edge : vertex.getMutableEdges()) {
                edge.setValue(new IntWritable(0));
            }
            vertex.setValue(new Text("0"));
        }

        // Phase 3 - Report triangles found
        if(getSuperstep() == 3) {
            Set<Long> edges = new HashSet<Long>();
            String V_value = "1";
            for(MutableEdge<LongWritable, IntWritable> edge : vertex.getMutableEdges()) {
                edges.add(edge.getTargetVertexId().get());
            }
            for(Message message : messages) {
                System.out.println("I am node " + vertex.getId() + ", and I received this: \"" + message + "\"");
                if(edges.contains(message.getTriadA().get()) && edges.contains(message.getTriadB().get())) {
                    System.out.println("I am node " + vertex.getId() + ", and I found the triangle (" + vertex.getId() + "," + message.getTriadA() + "," + message.getTriadB() + ")");
                    V_value += "@{" + vertex.getId() + "," + message.getTriadA() + "," + message.getTriadB() + "}";
                }
                else {
                    V_value = "false";
                }
            }
            vertex.setValue(new Text(V_value));
            vertex.voteToHalt();
        }

    }


    @Override
    public int run(String[] args) throws Exception {
        if (args.length != 2) {
            throw new IllegalArgumentException(
                    "run: Must have 4 arguments <input path> <output path> ");
        }
        GiraphConfiguration conf= new GiraphConfiguration();
        GiraphJob job = new GiraphJob(conf, "Find Triangles");
        job.getConfiguration().setComputationClass(Find_triangle.class);
        job.getConfiguration().setVertexInputFormatClass(
                InputFormat.class);
        job.getConfiguration().setVertexOutputFormatClass(
                OutputFormat.class);
        GiraphFileInputFormat.addVertexInputPath(job.getConfiguration(), new Path(args[0]));
        GiraphTextOutputFormat.setOutputPath(job.getInternalJob(), new Path(args[1]));
//        job.getConfiguration().setLong(String.valueOf(SimpleShortestPathsComputation.SOURCE_ID),
//                Long.parseLong(args[2]));
        job.getConfiguration().SPLIT_MASTER_WORKER.set(job.getConfiguration(), false);
        job.getConfiguration().setWorkerConfiguration(1, 1, 100.0f);
        if (job.run(true) == true) {
            return 0;
        } else {
            return -1;
        }
    }
    public static void main(String[] args) throws Exception {
        System.exit(ToolRunner.run(new Find_triangle(), args));
    }

    @Override
    public void setConf(Configuration configuration) {

    }
}
