package controllers;

import org.xmldb.api.DatabaseManager;
import org.xmldb.api.base.Collection;
import org.xmldb.api.base.Database;
import org.xmldb.api.modules.XMLResource;
import play.mvc.Controller;
import play.mvc.Result;
import views.html.index;


public class Application extends Controller {


    public static Result index() {
        return ok(index.render("Hellow World"));
    }

    public static Result simple() throws Exception {
        return ok(result().toString());
    }

    public static Object result() throws Exception {
        String DRIVER = "org.exist.xmldb.DatabaseImpl";
        String URI= "xmldb:exist://localhost:8080/exist/xmlrpc";
        String collectionPath = "/db/movies/";
        String resourceName = "movies.xml";

        Class cl = Class.forName(DRIVER);
        Database database = (Database) cl.newInstance();
        DatabaseManager.registerDatabase(database);
// get the collection
        Collection col = DatabaseManager.getCollection(URI + collectionPath);
// get the content of a document
        System.out.println("Get the content of " + resourceName);
        XMLResource res = (XMLResource) col.getResource(resourceName);
        if (res == null) {
            return "document not found!";
        } else {
            return res.getContent();
        }
    }

}
