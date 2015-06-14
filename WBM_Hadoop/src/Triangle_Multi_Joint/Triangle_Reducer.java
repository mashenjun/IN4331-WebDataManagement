package Triangle_Multi_Joint;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by mashenjun on 11-6-15.
 */
public class Triangle_Reducer extends Reducer<Text, Text,Text,Text> {
    static String alreadyfind="";
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        HashMap <String,String> R_MAP = new HashMap<>();
        HashMap <String,String> T_MAP = new HashMap<>();
        HashMap <String,String> S_MAP = new HashMap<>();
        String[] tempList;

        ArrayList<String> S_right = new ArrayList<>();
        ArrayList<String> S_left = new ArrayList<>();
        System.out.print("[");
        for (Text val: values){
            tempList = val.toString().split("-");
            System.out.print(val.toString()+",");
            if (tempList[0].equals("R")){
                R_MAP.put(tempList[1],tempList[2]);
            }
            else if (tempList[0].equals("T")){
                T_MAP.put(tempList[1],tempList[2]);
            }
            else if(tempList[0].equals("S")){
                S_right.add(tempList[1]);
                S_left.add(tempList[2]);

            }
//            switch (tempList[0]){
//                case "R" :
//                    R_MAP.put(tempList[1],tempList[2]);
//                case "T" :
//                    T_MAP.put(tempList[1],tempList[2]);
//                case "S" :
//                    System.out.print(tempList[0]);
//                    //System.out.print(tempList[1]+"-"+tempList[2]+",");
//                    S_MAP.put(tempList[1],tempList[2]);
//                default:
//            }
        }
        System.out.println("]");
        //System.out.println("the size of R and T is: "+R_MAP.size()+","+T_MAP.size());
        for (int i= 0; i<S_left.size();i++ ){
            String result = "";

            //System.out.println("====="+S_left.get(i)+"======"+S_right.get(i)+"======");
            if (R_MAP.containsKey(S_left.get(i))&&T_MAP.containsKey(S_right.get(i))){

                result += R_MAP.get(S_left.get(i)).toString();
                result += T_MAP.get(S_right.get(i)).toString();
                String testvalue = key.toString()+"-"+R_MAP.get(S_left.get(i)).toString()+"-"+T_MAP.get(S_right.get(i)).toString();
                boolean tempcheck = true;
                for (int j=0; j<alreadyfind.split(",").length;j++){
                    System.out.println(alreadyfind.split(",")[j]+"<><>"+testvalue+"@@@"+checktwoTriangle(alreadyfind.split(",")[j],testvalue));
                    if(checktwoTriangle(alreadyfind.split(",")[j],testvalue)){

                        tempcheck = false;

                        System.out.println(tempcheck);
                        break;
                    }
                }

                if (tempcheck){
                    context.write(key, new Text(result));
                    alreadyfind +=testvalue+",";
                }

            }
        }

//        for (Map.Entry<String,String> entry:S_MAP.entrySet()){
//
//            System.out.println("====="+entry.getKey()+"======"+entry.getValue()+"======");
//            if (R_MAP.containsKey(entry.getKey())&&T_MAP.containsKey(entry.getValue())) {
//                System.out.println("find one");
//                result += R_MAP.get(entry.getKey()).toString();
//                result += T_MAP.get(entry.getValue()).toString();
//                context.write(key, new Text(result));
//            }
//        }
    }

    public boolean checktwoTriangle(String A,String B){
        boolean result = false;
        if ( A.length()==B.length() && A.contains(B.split("-")[0]) && A.contains(B.split("-")[1]) && A.contains(B.split("-")[2])){
            result = true;
        }
        return result;
    }
}
