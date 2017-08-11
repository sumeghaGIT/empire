var deleteRecord = function(locations){
    swal({
            title: "",
            text: "Are you sure you want to delete record?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes",
            cancelButtonText: "Cancel",
            closeOnConfirm: true,
            closeOnCancel: true
        },
        function(isConfirm) {
            if (isConfirm) {
                $.ajax({
                    url : "delete/",
                    type : "POST",
                    data : {'id':1},
                    headers: { "X-CSRFToken": getCookie("csrftoken")},
                    beforeSend : function(xhr, settings){
                        crossDomain: false, // obviates need for sameOrigin test
                        console.log(" before deleteRecord function isConfirmed");
                        if (!csrfSafeMethod(settings.type)) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }                        
                    },
                    // handle a successful response
                    success : function(data) {
                        console.log("success");
                        swal('Success!',"Record successfully deleted.",'success');
                    },
                    // handle a non-successful response
                    error : function(xhr,errmsg,err) {
                        console.log(" failed deleteRecord function isConfirmed");
                    }
                });                
            }
        });    
};

// CSRF code
function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}