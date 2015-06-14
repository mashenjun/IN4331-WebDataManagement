package Execrise_4;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by mashenjun on 28-5-15.
 */
public class test {
    public static void main(String[] args) throws Exception {
        String text = "Tom Stall, a humble family man and owner of a \n" +
                "popular neighborhood restaurant, lives a quiet but \n" +
                "fulfilling existence in the Midwest. One night Tom \n" +
                "foils a crime at his place of business and, to his \n" +
                "chagrin, is plastered all over the news for his \n" +
                "heroics. Following this, mysterious people follow \n" +
                "the Stalls' every move, concerning Tom more than \n" +
                "anyone else. As this situation is confronted, more \n" +
                "lurks out over where all these occurrences have \n" +
                "stemmed from compromising his marriage, family \n" +
                "relationship and the main characters' former \n" +
                "relations in the process.";

        Pattern p = Pattern.compile("\\w+");
        Matcher m = p.matcher(text.toString());
        while (m.find()) {
            String matchedKey = m.group().toLowerCase();
            // remove names starting with non letters, digits, considered stopwords or containing other chars
            System.out.println(matchedKey);
            }
    }
}
