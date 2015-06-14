package Triangle_Multi_Joint;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.File;
import java.util.ArrayList;

/**
 * Created by mashenjun on 11-6-15.
 */
public class Triangle_Job {
    private static final String OUTPUT_PATH = "Triangle_output";
    private static final String INPUT_FOLDER = "Triangle_DataSet";
    public static void main(String[] args) throws Exception {
        String workingDir = System.getProperty("user.dir");

        ArrayList<String> textFiles = new ArrayList<String>();
        File dir = new File(workingDir+"/"+INPUT_FOLDER);
        for (File file : dir.listFiles()){
            if (file.getName().endsWith((".txt"))) {
                textFiles.add(INPUT_FOLDER+"/"+file.getName());

            }
        }
        Configuration conf = new Configuration();

	/* We expect two arguments */

//        if (args.length != 2) {
//            System.err.println("Usage: Exercise_2.AuthorsJob <in> <out>");
//            System.exit(2);
//        }

        /* Allright, define and submit the job */
        Job job = Job.getInstance(conf, "Execrise 5_2");
        //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
        job.setMapperClass(Triangle_Mapper.class);
        job.setReducerClass(Triangle_Reducer.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        /* Define the output type */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        /* Set the input and the output */
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(0)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(1)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(2)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(3)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(4)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(5)),TextInputFormat.class,WordCounting_Mapper.class);
//        MultipleInputs.addInputPath(job,new Path(textFiles.get(6)),TextInputFormat.class,WordCounting_Mapper.class);
        FileInputFormat.setInputPaths(job, textFiles.get(0) + ","
                + textFiles.get(1) + "," + textFiles.get(2));
        FileOutputFormat.setOutputPath(job, new Path(OUTPUT_PATH));

        /* Do it! */
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
