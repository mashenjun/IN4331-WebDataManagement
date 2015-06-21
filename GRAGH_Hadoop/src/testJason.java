import org.json.JSONArray;

/**
 * Created by mashenjun on 9-6-15.
 */
public class testJason {
    public static void main(String[] args) throws Exception {
        String line = "[1, 0, [[2, 0], [7, 0]]]";
        JSONArray json = new JSONArray(line.toString());
        System.out.println("fafdsa");
    }
}
