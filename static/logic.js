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
    var id = p.data('id');
    var done = 0;
    if($(self).is(':checked')) {
        done = 1
    }
    $.ajax({
        url: '/tasks/' + id,
        type: 'PUT',
        data: {
            'done': done
        },
        success: function(result) {
            if(result.task['done'] === 0) {
                p.removeClass("done");
            } else {
                p.addClass("done");
            }
        }
    })
}

function toggleImportant(e, id) {
    e = $(e);
    var importance = 1;
    if(e.hasClass("active")) {
        importance = 0;
    }
    $.ajax({
        url: '/tasks/' + id,
        type: 'PUT',
        data: {
            'important' : importance
        },
        success: function(result) {
            if(result.task['important'] === 0) {
                e.removeClass("active");
            } else {
                e.addClass("active");
            }
        }
    })
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