package Exercise_2;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by mashenjun on 27-5-15.
 */
public class Reducer2 extends Reducer<IntWritable, TextArrayWritable, NullWritable, Text> {

    @Override
    protected void reduce(IntWritable key, Iterable<TextArrayWritable> values,
                          Context context)
            throws IOException, InterruptedException {
        String artist_info = "";
        ArrayList<String> movie_info= new ArrayList<String>();
//        System.out.println("id "+key.toString()+" len "+ Iterators.size(values.iterator()));

//        while (values.iterator().hasNext()){
//            TextArrayWritable val = values.iterator().next();
//            System.out.println("."+val.toStrings()[0]+" "+val.toStrings()[1]+" "+val.toStrings()[2]+".");
//        }
        for (TextArrayWritable val : values) {
            String[] element = val.toStrings();
            //System.out.println("."+val.toStrings()[0]+" "+val.toStrings()[1]+" "+val.toStrings()[2]+".");

            if (element[0].equals("artist")){
                artist_info = element[1];
            }
            if (element[0].equals("movie")){
                movie_info.add(element[1]+"="+element[2]);
            }
        }
        System.out.println("=================");
        if (movie_info.size()>0) {
            for (int i = 0; i < movie_info.size(); i++) {
                String result =  artist_info + "\t" + movie_info.get(i).split("=")[0] + "\t" + movie_info.get(i).split("=")[1];
                System.out.println(result);
                context.write(null, new Text(result));
            }
        }
        System.out.println("=================");



    }
}
