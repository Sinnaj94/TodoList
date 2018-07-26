$(document).ready(function(){
    $('.task .name input').change(function (e) {
        var self = this;
        toggleDone(self);
    })
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
    var importance = 0;
    if(e.is(":checked")) {
        importance = 1;
    }
    $.ajax({
        url: '/tasks/' + id,
        type: 'PUT',
        data: {
            'important' : importance
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

function deleteCategory(id) {
    $.ajax(
        {
            url : '/categories/' + id,
            type: 'DELETE',
            success: function(result) {
                console.log(result);
                $('li[data-id="'+ result.category['category_id'] + '"').css('transition', 'none').fadeOut("normal", function() {
                    $(this).remove();
                });
            }
        }
    );
}