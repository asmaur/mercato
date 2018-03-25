$(document).ready(function(){

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
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

  if($('#contactForm').length){
    $('#contactForm').validator().on('submit', function (e) {
         
         var $this = $(this),
         $target = $(".form-response");
       if (e.isDefaultPrevented()) {
          $target.html("<div class='alert alert-danger'><p>Please select all required field.</p></div>");
       } else {
        var full_name = $("#full_name").val();
        var company_name = $("#company_name").val();
        var email = $("#mail").val();
        var phone = $("#telefone").val();
        var plan = $("#plan").val();
        var message = $("#message").val();
        var subject = $("#subject").val();
        e.preventDefault();
        values = {"full_name": full_name, "company_name": company_name, "email":email, "phone":phone, "plan":plan, "subject":subject ,"message":message}
        console.log(values);



        $.ajax({
              url: "contact/",              
              type: "POST",
              contentType: "application/json;charset=utf-8",             
              contentType: 'application/json',
              data: JSON.stringify({
               "full_name": full_name, "company_name": company_name, "email":email, "phone":phone, "plan":plan, "subject":subject, "message":message
                
              }),

              cache: false,

              beforeSend: function(xhr){

                $("#loader").show();
                $("#contactForm").hide();


                xhr.setRequestHeader("X-CSRFToken", csrftoken);           
              },              
           
              success: function(data){
                console.log(data);
                if (data['sent']) {


                    $this[0].reset();

                setTimeout(function(){  $("#loader").fadeOut();
                    $("#success").fadeIn(); $("#contactForm").fadeIn();}, 5000);

                    //$("#contactForm").show();
                   $("#success").fadeOut();

                 
                }else{
                    setTimeout(function(){  $("#loader").fadeOut();
                    $("#danger").fadeIn(); $("#contactForm").fadeIn();}, 5000);

                    //$("#contactForm").show();
                   $("#danger").fadeOut();


                }
                
              },

              error: function(){

              },

        }); 
        
       }
    });
  }
  
});