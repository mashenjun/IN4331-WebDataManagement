package Execrise_4;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Job2 {
    private static final String INPUT_PATH = "1-word-freq";
    private static final String OUTPUT_PATH = "2-word-count";
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Execrise 4-2");
        //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
        job.setMapperClass(WordCounting_Mapper2.class);
        job.setReducerClass(WordCounting_Reducer2.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        /* Define the output type */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        /* Set the input and the output */

        FileInputFormat.setInputPaths(job, new Path(INPUT_PATH+"/part-r-00000"));
        FileOutputFormat.setOutputPath(job, new Path(OUTPUT_PATH));

        /* Do it! */
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
