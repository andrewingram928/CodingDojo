$(document).ready(function() {

    $(".ninja").hover(function() {
        $(this).attr("holder", $(this).attr("src"));
        $(this).attr("src",  $(this).attr("alt"));
        $(this).attr("alt",  $(this).attr("holder"));
    });
});