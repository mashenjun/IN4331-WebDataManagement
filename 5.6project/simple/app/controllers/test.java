package controllers;

/**
 * Created by mashenjun on 30-4-15.
 */
import org.xmldb.api.DatabaseManager;
import org.xmldb.api.base.Collection;
import org.xmldb.api.base.Database;
import org.xmldb.api.modules.XMLResource;

public class test {
    protected static String DRIVER = "org.exist.xmldb.DatabaseImpl";
    protected static String URI= "xmldb:exist://localhost:8080/exist/xmlrpc";
    protected static String collectionPath = "/db/movies/";
    protected static String resourceName = "movies.xml";

    public static void main(String[] args) throws Exception {
        // initialize database driver
        Class cl = Class.forName(DRIVER);
        Database database = (Database) cl.newInstance();
        DatabaseManager.registerDatabase(database);
// get the collection
        Collection col = DatabaseManager.getCollection(URI + collectionPath);
// get the content of a document
        System.out.println("Get the content of " + resourceName);
        XMLResource res = (XMLResource) col.getResource(resourceName);
        if (res == null) {
            System.out.println("document not found!");
        } else {
            System.out.println(res.getContent());
        }
    }
}
