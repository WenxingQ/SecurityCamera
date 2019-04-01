window.onload = function() {
    // hide security camera page
    $("#main-page").hide();

    // login verification
    $("#btn-login").click(function (e) {
        e.preventDefault();
        var username = $("#username").val();
        var password = $("#password").val();
        if (username == "admin" && password == "verysecurepassword") {
            $("#login-page").hide();
            $("#main-page").show();
        }
        else
            alert("Unauthorized User")
    });

    $.get("https://objectstorage.us-ashburn-1.oraclecloud.com/n/wenxingqiu/b/bucket-1/o/", function(data){
        console.log(data);
        var cnt = 0;
        var finalOutString = "";
        $(data.objects).each(function() {
           console.log(data.objects[cnt].name);
           var outString = "";
           outString += "<div class=\"col-sm-6 col-md-4\">";
           outString += "<div class=\"thumbnail\">";
           outString += "<a href=\"https://objectstorage.us-ashburn-1.oraclecloud.com/n/wenxingqiu/b/bucket-1/o/";
           outString += data.objects[cnt].name;
           outString += "\" data-size=\"1600x1067\">";
           outString += "<img alt=\"picture\" src=\"https://objectstorage.us-ashburn-1.oraclecloud.com/n/wenxingqiu/b/bucket-1/o/";
           outString += data.objects[cnt].name;
           outString += "\" class=\"img-fluid\">";
           outString += "</a></div></div>";
           finalOutString += outString;
           cnt += 1;
        });
        $("#outputHere").html(finalOutString);
    });
};