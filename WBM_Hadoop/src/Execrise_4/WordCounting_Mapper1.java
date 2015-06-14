package Execrise_4;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by mashenjun on 28-5-15.
 */
public class WordCounting_Mapper1 extends Mapper<LongWritable, Text, Text,IntWritable> {

    private static String stopwords = "a about above after again against all am an and" +
            " any are aren't as at be because been before being" +
            " below between both but by can't cannot could couldn't" +
            " did didn't do does doesn't doing don't down during each" +
            " few for from further had hadn't has hasn't have haven't" +
            " having he he'd he'll he's her here here's hers herself" +
            " him himself his how how's i i'd i'll i'm i've" +
            " if in into is isn't it it's its itself let's" +
            " me more most mustn't my myself no nor not of" +
            " off on once only or other ought our ours ourselves" +
            " out over own same shan't she she'd she'll she's" +
            " should shouldn't so some such than that that's the their" +
            " theirs them themselves then there there's these they they'd they'll" +
            " they're they've this those through to too under until up very" +
            " was wasn't we we'd we'll we're we've were weren't what what's" +
            " when when's where where's which while who who's whom why why's" +
            " with won't would wouldn't you you'd you'll you're you've your" +
            " yours yourself yourselves";

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        // Compile all the words using regex
        String document = value.toString();
        Pattern p = Pattern.compile("\\w+");
        Matcher m = p.matcher(value.toString());

//
//        // Get the name of the file from the inputsplit in the context
        FileSplit fileSplit = (FileSplit)context.getInputSplit();
        String filename = fileSplit.getPath().getName();
        //System.out.println("File name: "+filename);
//
//        // build the values and write <k,v> pairs through the context
        StringBuilder valueBuilder = new StringBuilder();
        while (m.find()) {
            String matchedKey = m.group().toLowerCase();
            // remove names starting with non letters, digits, considered stopwords or containing other chars
//            if (!Character.isLetter(matchedKey.charAt(0)) || Character.isDigit(matchedKey.charAt(0))
//                    || googleStopwords.contains(matchedKey) || matchedKey.contains("_")) {
//                continue;
//            }
            if (!stopwords.contains(matchedKey)){
                valueBuilder.append(matchedKey);
                valueBuilder.append("@");
                valueBuilder.append(filename);
                //System.out.println("<"+valueBuilder.toString()+","+"1"+">");
                context.write(new Text(valueBuilder.toString()), new IntWritable(1));
                valueBuilder.setLength(0);
            }
        }
    }
}
