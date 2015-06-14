package Execrise_4;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.jobcontrol.ControlledJob;
import org.apache.hadoop.mapreduce.lib.jobcontrol.JobControl;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.File;
import java.util.ArrayList;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Job  {
    private static final String OUTPUT_PATH1 = "1-word-freq";
    private static final String INPUT_PATH2 = "1-word-freq";
    private static final String OUTPUT_PATH2 = "2-word-count";
    private static final String INPUT_PATH3 = "2-word-count";
    private static final String OUTPUT_PATH3 = "3-word-result";

    public static void main(String[] args)throws Exception {
        String workingDir = System.getProperty("user.dir");

        ArrayList<String> textFiles = new ArrayList<String>();
        File dir = new File(workingDir+"/datasets-small");
        for (File file : dir.listFiles()){
            if (file.getName().endsWith((".txt"))) {
                textFiles.add("datasets-small/"+file.getName());

            }
        }

        Configuration conf1 = new Configuration();

        //================== job1 =====================
        /* Allright, define and submit the job */
        Job job1= Job.getInstance(conf1, "Execrise 4-1");
        //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
        job1.setMapperClass(WordCounting_Mapper1.class);
        job1.setReducerClass(WordCounting_Reducer1.class);

        job1.setMapOutputKeyClass(Text.class);
        job1.setMapOutputValueClass(IntWritable.class);

        /* Define the output type */
        job1.setOutputKeyClass(Text.class);
        job1.setOutputValueClass(IntWritable.class);

        /* Set the input and the output */
        FileInputFormat.setInputPaths(job1, textFiles.get(0) + ","
                + textFiles.get(1) + "," + textFiles.get(2) + "," + textFiles.get(3) + "," + textFiles.get(4) + "," + textFiles.get(5) + "," + textFiles.get(6));
        FileOutputFormat.setOutputPath(job1, new Path(OUTPUT_PATH1));

        ControlledJob ctrljob1=new  ControlledJob(conf1);
        ctrljob1.setJob(job1);

        //===================== job2 ========================
        Configuration conf2 = new Configuration();
        Job job2 = Job.getInstance(conf2, "Execrise 4-2");
        //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
        job2.setMapperClass(WordCounting_Mapper2.class);
        job2.setReducerClass(WordCounting_Reducer2.class);

        job2.setMapOutputKeyClass(Text.class);
        job2.setMapOutputValueClass(Text.class);

        /* Define the output type */
        job2.setOutputKeyClass(Text.class);
        job2.setOutputValueClass(Text.class);

        /* Set the input and the output */

        FileInputFormat.setInputPaths(job2, new Path(INPUT_PATH2+"/part-r-00000"));
        FileOutputFormat.setOutputPath(job2, new Path(OUTPUT_PATH2));

        ControlledJob ctrljob2=new ControlledJob(conf2);
        ctrljob2.setJob(job2);
        ctrljob2.addDependingJob(ctrljob1);

        //===================== job3 ==========================
        Configuration conf3 = new Configuration();
        int filenumber = dir.listFiles().length;
        conf3.setInt("numberOfDocs", filenumber);
        Job job3 = Job.getInstance(conf3, "Execrise 4-2");
        //job.setJarByClass(MultipleInputs.class);
        /* Define the Mapper and the Reducer */
        job3.setMapperClass(WordCounting_Mapper3.class);
        job3.setReducerClass(WordCounting_Reducer3.class);

        job3.setMapOutputKeyClass(Text.class);
        job3.setMapOutputValueClass(Text.class);

        /* Define the output type */
        job3.setOutputKeyClass(Text.class);
        job3.setOutputValueClass(Text.class);

        /* Set the input and the output */

        FileInputFormat.setInputPaths(job3, new Path(INPUT_PATH3 + "/part-r-00000"));
        FileOutputFormat.setOutputPath(job3, new Path(OUTPUT_PATH3));

        ControlledJob ctrljob3=new ControlledJob(conf3);
        ctrljob3.setJob(job3);
        ctrljob3.addDependingJob(ctrljob2);

        JobControl jobCtrl=new JobControl("myctrl");
        jobCtrl.addJob(ctrljob1);
        jobCtrl.addJob(ctrljob2);
        jobCtrl.addJob(ctrljob3);

//        jobCtrl.run();
        /* Do it! */
        Thread  t=new Thread(jobCtrl);
        t.start();
        while(true){
            if(jobCtrl.allFinished()) {
                FileSystem fs1= FileSystem.get(conf1);
                FileSystem fs2= FileSystem.get(conf2);
                Path op1 = new Path (OUTPUT_PATH1);
                Path op2 = new Path (OUTPUT_PATH2);
                fs1.delete(op1, true);
                fs2.delete(op2, true);

                System.out.println(jobCtrl.getSuccessfulJobList());

                jobCtrl.stop();
                break;
            }
        }
    }
}

