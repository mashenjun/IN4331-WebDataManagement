package Triangle_Multi_Joint;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.codehaus.jettison.json.JSONArray;
import org.codehaus.jettison.json.JSONException;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by mashenjun on 11-6-15.
 */
public class Triangle_Mapper extends Mapper<LongWritable, Text, Text, Text> {
    private HashMap<String,JSONArray> temprelation_1 = new HashMap<>();
    private HashMap<String,ArrayList> temprelation_2 = new HashMap<>();
    public boolean dealSdata = false;
    public void map(LongWritable key, Text value, Mapper.Context context) throws IOException, InterruptedException {
        // Compile all the words using regex
        String document = value.toString();
        JSONArray data = null;
        Integer len = null;
        FileSplit fileSplit = (FileSplit)context.getInputSplit();
        String filename = fileSplit.getPath().getName().toString();
        try {
            data= new JSONArray(document);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        len = data.length();
        switch (filename) {
            case "SetR.txt" :
                for (int i =0; i<len;i++){
                    try {
                        String  left = ((JSONArray)data.get(i)).getString(0);
                        String right = ((JSONArray)data.get(i)).getString(1);
                        Text R_key = new Text(left);
                        //Text R_key = new Text(right.hashCode()+"");
                        Text R_value = new Text("R-"+right.hashCode()+"-"+right.toString());
                        context.write(R_key,R_value);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
            case "SetT.txt" :
                for (int i =0; i<len;i++){
                    try {
                        String  left = ((JSONArray)data.get(i)).getString(0);
                        String right = ((JSONArray)data.get(i)).getString(1);
                        Text R_key = new Text(right);
                        Text R_value = new Text("T-"+left.hashCode()+"-"+left.toString());
                        context.write(R_key,R_value);


                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                }

            case "SetS.txt" :
                ArrayList<String> temprightlist = new ArrayList<>();
                for (int i =0; i<len;i++){
                    try {
                        String  left = ((JSONArray)data.get(i)).getString(0);
                        String right = ((JSONArray)data.get(i)).getString(1);
                        //Text R_key = new Text(left);
                        //Text R_value = new Text("S-"+left.hashCode()+"-"+right.hashCode());
                        //context.write(R_key,R_value);
                        temprightlist.add(right);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                try {
                    temprelation_1.put(((JSONArray)data.get(0)).getString(0),data);
                    temprelation_2.put(((JSONArray)data.get(0)).getString(0),temprightlist);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            default:

        }

//        for (Map.Entry<String,ArrayList> entry:temprelation_2.entrySet()){
//            String temp_kep = entry.getKey();
//            Text R_key = new Text(temp_kep);
//            ArrayList<String> temp_find_value = entry.getValue();
//            for (String val:temp_find_value){
//                System.out.println("------"+val+"-----");
//                JSONArray temp_right_list = temprelation_1.get(val);
//                for (int i =0; i<temp_right_list.length();i++){
//                    try {
//                        String  left = ((JSONArray)temp_right_list.get(i)).getString(0);
//                        String right = ((JSONArray)temp_right_list.get(i)).getString(1);
//                        //Text R_key = new Text(left);
//                        Text R_value = new Text("S-"+left.hashCode()+"-"+right.hashCode());
//                        context.write(R_key,R_value);
//                    } catch (JSONException e) {
//                        e.printStackTrace();
//                    }
//                }
//            }
//        }
    }

    @Override
    public void cleanup (Mapper.Context context) throws IOException, InterruptedException {
        FileSplit fileSplit = (FileSplit)context.getInputSplit();
        String filename = fileSplit.getPath().getName().toString();
        if(filename.equals("SetS.txt")) {

            for (Map.Entry<String, ArrayList> entry : temprelation_2.entrySet()) {
                String temp_kep = entry.getKey();
                Text R_key = new Text(temp_kep);
                String alreallySend = "";
                ArrayList<String> temp_find_value = entry.getValue();
                for (String val : temp_find_value) {
                    //System.out.println("------" + val + "-----");
                    JSONArray temp_right_list = temprelation_1.get(val);
                    for (int i = 0; i < temp_right_list.length(); i++) {
                        try {
                            String left = ((JSONArray) temp_right_list.get(i)).getString(0);
                            String right = ((JSONArray) temp_right_list.get(i)).getString(1);
                            if (alreallySend.contains(left.hashCode() + "-" + right.hashCode())==false && alreallySend.contains(right.hashCode() + "-" + left.hashCode())==false) {
                                Text R_value = new Text("S-" + left.hashCode() + "-" + right.hashCode());
                                System.out.println(R_key.toString() + "***" + left + "^" + right);
                                context.write(R_key, R_value);
                                alreallySend += left.hashCode() + "-" + right.hashCode()+",";
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                            //Text R_key = new Text(left);

                    }

                }
            }
        }
    }

}
