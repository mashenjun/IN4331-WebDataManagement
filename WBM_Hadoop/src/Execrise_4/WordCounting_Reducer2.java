package Execrise_4;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by mashenjun on 29-5-15.
 */
public class WordCounting_Reducer2 extends Reducer<Text, Text,Text,Text> {
    private Text wordAtDoc = new Text();
    private Text wordAvar = new Text();

    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        DecimalFormat df = new DecimalFormat("0.000");
        int sumOfWordsInDocument = 0;
        Map<String, Integer> tempCounter = new HashMap<String, Integer>();
        for (Text val : values) {

            String[] wordCounter = val.toString().split("=");
            tempCounter.put(wordCounter[0], Integer.valueOf(wordCounter[1]));
            sumOfWordsInDocument += Integer.parseInt(val.toString().split("=")[1]);
        }
        for (String wordKey : tempCounter.keySet()) {
            this.wordAtDoc.set(wordKey + "@" + key.toString());
            //double percent = (double)tempCounter.get(wordKey)/(double)sumOfWordsInDocument;
            this.wordAvar.set(String.valueOf( tempCounter.get(wordKey) + "/" + sumOfWordsInDocument));
            context.write(this.wordAtDoc, this.wordAvar);
        }
    }

}
