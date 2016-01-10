$(document).ready(function() {

$('.log_in').click(function(){
	$('#login_modal').modal();
});

$('.switch').on('click', function(){
	if($('.modal-body.login_form').is(':visible')) {
		$('.login_form').hide();
		$('.registration_form').show();
	}
	else{
		$('.registration_form').hide();
		$('.login_form').show();
	}
});

$('.modal').on('hidden.bs.modal', function() {
	console.log('foo');
	$('.registration_form').hide();
	$('.login_form').show();
});

});
