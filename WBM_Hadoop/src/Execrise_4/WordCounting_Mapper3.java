package Execrise_4;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Mapper3 extends Mapper<LongWritable, Text, Text,Text> {
    private Text key = new Text();
    private Text result = new Text();
    public void map(LongWritable key, Text value, Mapper.Context context) throws IOException, InterruptedException {
        String[] wordAndDocFrequency = value.toString().split("\t");
        String[] wordAndDoc = wordAndDocFrequency[0].split("@");
        this.key.set(wordAndDoc[0]);
        this.result.set(wordAndDoc[1]+"="+wordAndDocFrequency[1]);
        System.out.println("<" + wordAndDoc[0]+","+wordAndDoc[1]+"="+wordAndDocFrequency[1]+">");
        context.write(this.key,result);
    }
}
