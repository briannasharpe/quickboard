$(document).ready(function () {
    $("p").click(function () {
        $("form").toggle(1000);
    });
});

$('message a').click(function () {
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});