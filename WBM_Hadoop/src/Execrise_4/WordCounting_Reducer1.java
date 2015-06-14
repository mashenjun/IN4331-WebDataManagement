package Execrise_4;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

/**
 * Created by mashenjun on 28-5-15.
 */
public class WordCounting_Reducer1 extends Reducer<Text, IntWritable,Text,IntWritable> {

    protected void reduce(Text key, Iterable<IntWritable> values,
                          Context context)
            throws IOException, InterruptedException {
        int total_count=0;
        for (IntWritable val : values) {
            //System.out.print(val.toString()+" ");
                total_count = total_count+val.get();
//            String[] element = val.toStrings();
//            //System.out.println("."+val.toStrings()[0]+" "+val.toStrings()[1]+" "+val.toStrings()[2]+".");
//
//            if (element[0].equals("artist")){
//                artist_info = element[1];
//            }
//            if (element[0].equals("movie")){
//                movie_info.add(element[1]+"="+element[2]);
//            }
        }
        System.out.println(key+" "+total_count);
        context.write(key,new IntWritable(total_count));


    }
}
