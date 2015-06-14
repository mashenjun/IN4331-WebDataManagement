package Execrise_4;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Mapper2 extends  Mapper<LongWritable, Text, Text,Text>{
    private Text docName = new Text();
    private Text wordAndCount = new Text();

    public void map(LongWritable key, Text value, Mapper.Context context) throws IOException, InterruptedException {
        String[] wordAndDocCounter = value.toString().split("\t");
        String[] wordAndDoc = wordAndDocCounter[0].split("@");
        this.docName.set(wordAndDoc[1]);
        this.wordAndCount.set(wordAndDoc[0] + "=" + wordAndDocCounter[1]);
        //System.out.println("<" + wordAndDoc[1]+","+wordAndDoc[0] + "=" + wordAndDocCounter[1]+">");
        context.write(this.docName, this.wordAndCount);

    }
}
