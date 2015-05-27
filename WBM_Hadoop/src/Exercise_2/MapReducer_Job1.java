package Exercise_2;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.mahout.text.wikipedia.XmlInputFormat;

/**
 * Created by mashenjun on 26-5-15.
 */
public class MapReducer_Job1 {
    public static void main(String[] args) throws Exception {

	/*
	 * Load the Haddop configuration. IMPORTANT: the
	 * $HADOOP_HOME/conf directory must be in the CLASSPATH
	 */
        Configuration conf = new Configuration();

        conf.set("xmlinput.start","<movies>");
        conf.set("xmlinput.end", "</movies>");


	/* We expect two arguments */

        if (args.length != 2) {
            System.err.println("Usage: Exercise_2.AuthorsJob <in> <out>");
            System.exit(2);
        }

	/* Allright, define and submit the job */
        Job job = Job.getInstance(conf, "Execrise 2.1");
        job.setInputFormatClass(XmlInputFormat.class);

	/* Define the Mapper and the Reducer */
        job.setMapperClass(Movie_ref_Mapper.class);
        job.setReducerClass(Reducer1.class);

        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(TextArrayWritable.class);

	/* Define the output type */
        job.setOutputKeyClass(IntWritable.class);
        job.setOutputValueClass(Text.class);

	/* Set the input and the output */
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

	/* Do it! */
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
