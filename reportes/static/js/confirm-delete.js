function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(document).ready(function() {

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  // This function must be customized
  var onDelete = function(){
    var url =this.href;
    swal({
      title: "Estas seguro?",
      text: "Se borrara completamente el registro!",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#DD6B55",
      confirmButtonText: "Si, borralo!",
      cancelButtonText: "Cancelar",
      closeOnConfirm: false
    }, function(){
      $.post(url, function(data) {
        if (data.result == "ok"){
          swal({
            title: "El registro ha sido borrado.",
            type: "success" ,
          },function(){
            location.reload();
          });
        } else {
          var msg="Algo salio mal."
          if(data.message){
            msg=data.message
          }
          swal("Ups!", msg, "warning");
        }
      }).fail(function(error) {
        swal("Eliminado!", "Error.", "warning");
      });
    });
    return false;
  }

  $(".delete").click(onDelete);
});
