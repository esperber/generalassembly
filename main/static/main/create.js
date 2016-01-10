var step = 900;
var question_counter = 1;
			   
current = $("#scroll-items").css('left'); 
console.log(current);

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

$(".description").click(function() {
	$("#submit").hide()
	$("#previous").hide();
	$("#next").show();
	$("#scroll-items").animate({
        	left: "0px"
    	});
});

$(".location").click(function() {
		$("#submit").hide()
		$("#previous").show();
		$("#next").show();
        $("#scroll-items").animate({
                left: "-900px"
        });
});

$(".price").click(function() {
		$("#submit").hide()
		$("#previous").show();
		$("#next").show();
        $("#scroll-items").animate({
                left: "-1800px"
        });
});

$(".pictures").click(function() {
		$("#submit").hide()
		$("#previous").show();
		$("#next").show();
        $("#scroll-items").animate({
                left: "-2700px"
        });
});

$(".questionaire").click(function() {
		$("#submit").hide()
		$("#previous").show();
		$("#next").show();
        $("#scroll-items").animate({
                left: "-3600px"
        });
});

$(".confirmation").click(function() {
		$("#previous").show();
		$("#next").hide();
		$("#submit").show()
        $("#scroll-items").animate({
                left: "-4500px"
        });
});


$("#next").on("click", function() {
    current = $("#scroll-items").css('left');
    console.log(current);
    if(current=='900px'){
        $("#previous").hide()
    }
    else{
        $("#previous").show()
    }
    if(current=='-3600px'){
        $("#next").hide()
        $("#submit").show()
    }
    else{
    	$("#submit").hide()
        $("#next").show()  
    }
    $("#scroll-items").animate({
        left: "-=" + step + "px"
    });
});

$("#previous").on("click", function() {
    $("#scroll-items").animate({
        left: "+=" + step + "px"
    });
    
    current = $("#scroll-items").css('left');
    if(current=='-900px'){
        $("#previous").hide();
    }
    else{
        $("#previous").show();
    }
	$("#submit").hide()
    $("#next").show()
    

});

Dropzone.options.myAwesomeDropzone = { // The camelized version of the ID of the form element
  url: '/main/upload/image/', 
  uploadMultiple: true,
  parallelUploads: 100,
  previewsContainer: '.preview-drop',
  previewTemplate: document.querySelector('#preview-template').innerHTML,
  maxFiles: 100,
  dictResponseError: 'Error uploading file!',
  headers: {'X-CSRF-Token': getCookie('csrftoken')},

  // The setting up of the dropzone
  init: function() {
    var myDropzone = this;
	
    // First change the button to actually tell Dropzone to process the queue.
	this.element.querySelector("button").addEventListener("click", function(e) {
      myDropzone.processQueue();
    });
	
    
    this.on("sending", function(files, response) {
    	console.log("sending");
    	// Your other code goes here...
	});
	
    this.on("success", function(files, response) {
    	console.log(files)
		console.log("complete");
    });
    
    this.on("errormultiple", function(files, response) {
      // Gets triggered when there was an error sending the files.
      // Maybe show form again, and notify user of error
    });
  }

}


$(".add-question").on("click", function() {
	question_html = $('.question-event:first').clone();
	question_html.find('.number_circle span').text(question_counter+1)
	$(".questionaire-view").append(question_html);
	question_counter = question_counter+1;
});

