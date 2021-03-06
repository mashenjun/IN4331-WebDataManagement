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


import org.apache.giraph.graph.Vertex;
import org.apache.giraph.io.formats.TextVertexOutputFormat;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.TaskAttemptContext;

import java.io.IOException;

public class OutputFormat extends TextVertexOutputFormat<LongWritable, Text, IntWritable> {

    @Override
    public TextVertexWriter createVertexWriter(
            TaskAttemptContext context) throws IOException,
            InterruptedException {

        return new TrianglesVertexWriter();
    }

    public class TrianglesVertexWriter extends TextVertexWriter {

        private Text line = new Text();
        private StringBuilder sb = new StringBuilder();

        public void writeVertex(
                Vertex<LongWritable, Text, IntWritable> vertex)
                throws IOException, InterruptedException {
            if (vertex.getValue().toString().equalsIgnoreCase("false")==false){
                String[] V_value = vertex.getValue().toString().split("@");

                for (int i =1; i<V_value.length;i++){
                    sb.append(vertex.getId());
                    sb.append(" report a triangle: ");
                    sb.append(V_value[i]);
                    line.set(sb.toString());
                    getRecordWriter().write(null, line);
                    sb.setLength(0);
                }

            }
//            sb.append(vertex.getId());
//            for(Edge<LongWritable, IntWritable> edge : vertex.getEdges()) {
//                sb.append(" ");
//                sb.append(edge.getTargetVertexId() + ":" + edge.getValue());
//            }
//            line.set(sb.toString());
//
//            getRecordWriter().write(null, line);
//            sb.setLength(0);

        }

    }
}