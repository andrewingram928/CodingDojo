$(document).ready(function() {

    $(".ninja").click(function() {
        $(this).hide();
    });

    $(".restore").click(function() {
        $(".ninja").show();
    })
});