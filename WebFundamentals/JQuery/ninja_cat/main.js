$(document).ready(function() {

    $("img").click(function() {
        $(this).attr("holder", $(this).attr("src"));
        $(this).attr("src", $(this).attr("data-alt-src"));
        $(this).attr("data-alt-src", $(this).attr("holder"));
       });
});