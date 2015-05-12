/**
 * Created by mashenjun on 29-4-15.
 */
import org.exist.xmldb.XQueryService;
import org.xmldb.api.DatabaseManager;
import org.xmldb.api.base.*;

    public class ExistQuery {
        protected static String DRIVER = "org.exist.xmldb.DatabaseImpl";
        protected static String URI = "xmldb:exist://localhost:8080/exist/xmlrpc";
        protected static String collectionPath = "/db/movies";
        protected static String resourceName = "movies.xml";
        public static void main(String[] args) throws Exception {
// initialize database driver
            Class cl = Class.forName(DRIVER);
            Database database = (Database) cl.newInstance();
            DatabaseManager.registerDatabase(database);
// get the collection
            Collection col = DatabaseManager.getCollection(URI + collectionPath);
// query a document
            String xQuery = "for $x in doc('" + resourceName + "')//title "
                    + "return data($x)";
            System.out.println("Execute xQuery = " + xQuery);
// Instantiate a XQuery service
            XQueryService service = (XQueryService) col.getService("XQueryService",
                    "1.0");
            service.setProperty("indent", "yes");
// Execute the query, print the result
            ResourceSet result = service.query(xQuery);
            ResourceIterator i = result.getIterator();
            while (i.hasMoreResources()) {
                Resource r = i.nextResource();
                System.out.println((String) r.getContent());
            }
        }
    }
