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


import org.apache.giraph.edge.DefaultEdge;
import org.apache.giraph.edge.Edge;
import org.apache.giraph.graph.Vertex;
import org.apache.giraph.io.formats.TextVertexInputFormat;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
import org.json.JSONArray;
import org.json.JSONException;

import java.io.IOException;
import java.util.ArrayList;

public class InputFormat extends TextVertexInputFormat<LongWritable, Text, IntWritable>{
    JSONArray json;
    Text text;

    @Override
    public TextVertexReader createVertexReader(
            InputSplit split, TaskAttemptContext context) throws IOException {
        return new ComponentisationVertexReader();
    }

    public class ComponentisationVertexReader extends TextVertexReader {

        @Override
        public boolean nextVertex() throws IOException, InterruptedException {
            return getRecordReader().nextKeyValue();
        }

        @Override
        public Vertex<LongWritable, Text, IntWritable> getCurrentVertex() throws IOException, InterruptedException {
            Text line = getRecordReader().getCurrentValue();
            try {
                json = new JSONArray(line.toString());
            } catch (JSONException e) {
                e.printStackTrace();
            }
            LongWritable id = null;
            try {
                id = new LongWritable(json.getInt(0));
            } catch (JSONException e) {
                e.printStackTrace();
            }


            ArrayList<Edge<LongWritable, IntWritable>> edgeIdList = new ArrayList<Edge<LongWritable, IntWritable>>();

            if(json.length() > 1) {
                try {
                    for (int i = 0; i < ((JSONArray)json.get(2)).length(); i++) {
                        DefaultEdge<LongWritable, IntWritable> edge = new DefaultEdge<LongWritable, IntWritable>();
                        edge.setTargetVertexId(new LongWritable(json.getJSONArray(2).getJSONArray(i).getLong(0)));
                        edge.setValue(new IntWritable(0));
                        edgeIdList.add(edge);
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
            
            Vertex<LongWritable, Text, IntWritable> vertex = getConf().createVertex();

            try {
                vertex.initialize(id, new Text(json.getString(1)), edgeIdList);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            return vertex;
        }
    }

}