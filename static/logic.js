$(document).ready(function(){
    $('.task .name input').change(function (e) {
        var self = this;
        toggleDone(self);
    })
    /*$('.task').click(function(e) {
        if(!($(e.target).is('button') || $(e.target.parentElement).is('button'))) {
            $(this).find('.name input').click();
        }
    });*/
});

function toggleDone(self) {
    var p = $(self).parent().parent();
    if($(self).is(':checked')) {
        p.addClass("done");
    } else {
        p.removeClass("done");
    }
}

function toggleImportant(e) {
    e = $(e);
    if(e.hasClass("active")) {
        // TODO: Remove in db
        e.removeClass("active");
    } else {
        // TODO: add in db
        e.addClass("active");
    }
    $.ajax("/task")
}

function deleteTask(id) {
    $.ajax(
        {
            url : '/tasks/' + id,
            type: 'DELETE',
            success: function(result) {
                $('li[data-id="'+ result.task['task_id'] + '"').css('transition', 'none').fadeOut("normal", function() {
                   $(this).remove();
                });
            }
        }
    );
}