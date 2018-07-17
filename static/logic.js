$(document).ready(function(){
    $('.task .name input').change(function (e) {
        var p = $(this).parent().parent();
        if($(this).is(':checked')) {
            p.addClass("done");
        } else {
            p.removeClass("done");
        }
    })
});

function toggleImportant(e) {
    e = $(e);
    if(e.hasClass("active")) {
        // TODO: Remove in db
        e.removeClass("active");
    } else {
        // TODO: add in db
        e.addClass("active");
    }
}