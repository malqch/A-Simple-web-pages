$(function () {
    $(".movies_add").click(function () {
        // alert("收到了")
        // var movieid =
        var movieid = $(this).attr("movie_id");

        $.get("http://127.0.0.1:8000/amovies/addtomycollect/",{"movieid":movieid},function (data) {
            alert(data["msg"]);
        })
    });
//    删除
    $(".movies_del").click(function () {
        // alert("点到了")
        var sub = $(this);
        var mycollectid = sub.attr("mycollectid");

        $.get("http://127.0.0.1:8000/amovies/delmycollect/",{"mycollectid":mycollectid},function (data) {
            alert(data["msg"]);
            sub.parents("li").remove();
            // sub.remove();
        })
    })

});