package Exercise_2;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapreduce.Mapper;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.IOException;
import java.io.StringReader;

/**
 * Created by mashenjun on 26-5-15.
 */

public class Movie_ref_Mapper extends Mapper<LongWritable, Text, IntWritable,TextArrayWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text author = new Text();
    private IntWritable id = new  IntWritable();
    private Text content = new Text();
    private TextArrayWritable  text_list = new TextArrayWritable();
    private Text movie_title,role,Birth,TName = new Text();

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
       String document = value.toString();
       System.out.println("‘" + document + "‘");


        DocumentBuilder db = null;
        try {
            db = DocumentBuilderFactory.newInstance().newDocumentBuilder();
        } catch (ParserConfigurationException e) {
            e.printStackTrace();
        }
        InputSource is = new InputSource();
        is.setCharacterStream(new StringReader(document));

        Document doc = null;
        try {
            doc = db.parse(is);
        } catch (SAXException e) {
            e.printStackTrace();
        }

        NodeList node_movie = doc.getElementsByTagName("movie");
        NodeList node_artist = doc.getElementsByTagName("artist");


        for (int i= 0; i<node_movie.getLength();i++){
            NodeList node_id;
            String temp_title = ((Element)node_movie.item(i)).getElementsByTagName("title").item(0).getTextContent();
            movie_title = new Text(temp_title);
            node_id = ((Element)node_movie.item(i)).getElementsByTagName("actor");
                for (int j= 0; j<node_id.getLength();j++){
                    int temp_id = Integer.parseInt(((Element) node_id.item(j)).getAttribute("id"));
                    this.id = new IntWritable(temp_id);
                    String temp_role = ((Element) node_id.item(j)).getAttribute("role");
                    role = new Text(temp_role);
                    text_list.set(new Writable[]{new Text("movie"),movie_title,role});
                    System.out.println(temp_id+"___"+ temp_role+"_____"+temp_title);
//                    text_list = new Text[]{new Text("movie"),movie_title,role};
                    context.write(this.id, text_list );
                }
//             this.id = node_movie.item(i).
        }

        for (int i =0; i<node_artist.getLength();i++){
            this.id = new IntWritable( Integer.parseInt(((Element) node_artist.item(i)).getAttribute("id")) );
            String Fname =  ((Element) node_artist.item(i)).getElementsByTagName("first_name").item(0).getTextContent();
            System.out.println("++++Fname " + Fname + "++++");
            String Lname = ((Element) node_artist.item(i)).getElementsByTagName("last_name").item(0).getTextContent();
            System.out.println("++++Lname " + Lname + "++++");
            TName = new Text(Lname+" "+Fname);
            Birth = new Text( ((Element) node_artist.item(i)).getElementsByTagName("birth_date").item(0).getTextContent() );
            text_list.set(new Writable[]{new Text("artist"),TName,Birth});
//            text_list = new Text[]{new Text("artist"),TName,Birth};
            context.write(this.id, text_list);
        }



	  /* Open a Java scanner object to parse the line */
//        Scanner line = new Scanner(value.toString());
//        line.useDelimiter("\t");
//        author.set(line.next());
//        context.write(author, one);
    }
}
