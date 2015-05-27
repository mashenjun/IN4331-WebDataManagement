package Exercise_2;

import org.apache.hadoop.io.ArrayWritable;
import org.apache.hadoop.io.Text;

/**
 * Created by mashenjun on 27-5-15.
 */
public class TextArrayWritable extends ArrayWritable {
    public TextArrayWritable() {
        super(Text.class);  // 这里，根据自己要实现的数组类型，填入对应实现了writable接口的类型，比方说IntWritable
    }
}
