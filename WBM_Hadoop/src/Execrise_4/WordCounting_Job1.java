package Execrise_4;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.File;
import java.util.ArrayList;

/**
 * Created by mashenjun on 28-5-15.
 */
public class WordCounting_Job1 {
    // where to put the data in hdfs when we're done
    private static final String OUTPUT_PATH = "1-word-freq";

    // where to read the data from.
//    private static final String INPUT_PATH1 = "datasets-small/A History of Violence.txt";
//    private static final String INPUT_PATH2 = "datasets-small/.txt";
//    private static final String INPUT_PATH3 = "datasets-small/A History of Violence.txt";
//    private static final String INPUT_PATH4 = "datasets-small/A History of Violence.txt";
//    private static final String INPUT_PATH5 = "datasets-small/A History of Violence.txt";
//    private static final String INPUT_PATH6 = "datasets-small/A History of Violence.txt";
    public static void main(String[] args) throws Exception {
        String workingDir = System.getProperty("user.dir");

        ArrayList<String> textFiles = new ArrayList<String>();
        File dir = new File(workingDir+"/datasets-small");
        for (File file : dir.listFiles()){
            if (file.getName().endsWith((".txt"))) {
                textFiles.add("datasets-small/"+file.getName());

            }
        }
        Configuration conf = new Configuration();

	/* We expect two arguments */

//        if (args.length != 2) {
//            System.err.println("Usage: Exercise_2.AuthorsJob <in> <out>");
//            System.exit(2);
//        }

        /* Allright, define and submit the job */
            Job job = Job.getInstance(conf, "Execrise 4-1");
            //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
            job.setMapperClass(WordCounting_Mapper1.class);
            job.setReducerClass(WordCounting_Reducer1.class);

            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(IntWritable.class);

        /* Define the output type */
            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(IntWritable.class);

        /* Set the input and the output */
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(0)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(1)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(2)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(3)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(4)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(5)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(6)),TextInputFormat.class,WordCounting_Mapper.class);
        FileInputFormat.setInputPaths(job, textFiles.get(0) + ","
                + textFiles.get(1)+","+textFiles.get(2)+","+textFiles.get(3)+","+textFiles.get(4)+","+textFiles.get(5)+","+textFiles.get(6));
            FileOutputFormat.setOutputPath(job, new Path(OUTPUT_PATH));

        /* Do it! */
            System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
