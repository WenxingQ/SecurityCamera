package controller;
import static spark.Spark.*;

public class HomeSecurityController {
    public static void main(String[] args)  {
        staticFiles.location("/public");
        get("/", (req, res) -> {res.redirect("/index.html"); return null;});
    }
}
