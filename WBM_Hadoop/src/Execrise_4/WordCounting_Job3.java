package Execrise_4;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.File;
import java.util.ArrayList;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Job3 {
    private static final String INPUT_PATH = "2-word-count";
    private static final String OUTPUT_PATH = "3-word-result";
    public static void main(String[] args) throws Exception {
        String workingDir = System.getProperty("user.dir");
        ArrayList<String> textFiles = new ArrayList<String>();
        File dir = new File(workingDir+"/datasets-small");
        int filenumber = dir.listFiles().length;
        Configuration conf = new Configuration();
        conf.setInt("numberOfDocsInCorpus", filenumber);

        Job job = Job.getInstance(conf, "Execrise 4-2");
        //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
        job.setMapperClass(WordCounting_Mapper3.class);
        job.setReducerClass(WordCounting_Reducer3.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        /* Define the output type */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        /* Set the input and the output */

        FileInputFormat.setInputPaths(job, new Path(INPUT_PATH + "/part-r-00000"));
        FileOutputFormat.setOutputPath(job, new Path(OUTPUT_PATH));

        /* Do it! */
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
