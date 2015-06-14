package Execrise_4;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Reducer3 extends Reducer<Text, Text,Text,Text> {
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException,
            InterruptedException {
        DecimalFormat df = new DecimalFormat("0.000");
        int totalfilenumber = context.getConfiguration().getInt("numberOfDocs", 0);
        int wordtofilenumber = 0;
        String result ="";
        ArrayList<String> temp = new ArrayList<String>();
        //String [] filenameandfequence=new String[]{};
        Map<String, String> tempFrequencies = new HashMap<String, String>();
        for (Text val : values) {
            wordtofilenumber++;
            temp.add(val.toString());
        }
        for (String element : temp){
            String [] filenameandfequence = element.split("=");
            String[] termFandTnumber = filenameandfequence[1].split("/");
            double a = Double.parseDouble(termFandTnumber[0]);
            double b = Double.parseDouble(termFandTnumber[1]);
            double percent =  a/b;
            result= result+"<"+filenameandfequence[0]+" "+df.format(percent).toString()+">";
        }
        double idf = Math.log10((double)totalfilenumber/(double)wordtofilenumber);
        result = result+"["+df.format(idf).toString()+"]";
        context.write(key,new Text(result));

    }
}
