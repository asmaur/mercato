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

  if($('#newsForm').length){
    $('#newsForm').validator().on('submit', function (e) {
         
         var $this = $(this),
         $target = $(".form-response");
       if (e.isDefaultPrevented()) {
          $target.html("<div class='alert alert-danger'><p>Please select all required field.</p></div>");
       } else {
        var name = $("#name").val();

        var email = $("#email").val();
        var phone = $("#phone").val();

        e.preventDefault();
        values = {"full_name": name, "email":email, "fone_number":phone }
        //console.log(values);



        $.ajax({
              url: "news/",
              type: "POST",
              contentType: 'application/json',
              data: JSON.stringify({"full_name": name, "email":email, "fone_number":phone }),
              
              cache: false,

              beforeSend: function(xhr){

                $("#wrong").hide();
                $("#check").hide();
                $("#spin").show();
                //$("#contactForm").hide();


                xhr.setRequestHeader("X-CSRFToken", csrftoken);           
              },              
           
              success: function(data){
                console.log(data['sent']);
                if (data['sent']) {


                    $this[0].reset();

                setTimeout(function(){  $("#spin").fadeOut();
                    $("#checked").fadeIn();}, 3000);

                    //$("#contactForm").show();
                   //$("#success").fadeOut();

                 
                }else{
                    setTimeout(function(){  $("#spin").fadeOut();
                    $("#wrong").fadeIn(); }, 3000);


                }
                
              },

              error: function(){

              },

        }); 
        
       }
    });
  }
  
});