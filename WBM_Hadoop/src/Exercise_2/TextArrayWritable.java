package Exercise_2;

import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.Text;

/**
 * Created by mashenjun on 27-5-15.
 */
public class TextArrayWritable extends ArrayWritable {
    public TextArrayWritable() {
        super(Text.class);  // In
    }
}
