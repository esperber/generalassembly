$(document).ready(function() {
	dates = []
	$('li').hover(function(){
    		$(this).addClass('active');
	}, function(){
		$(this).removeClass('active');
	});

	for(var selected_day in dates){
                $('.fc-day[data-date="' + selected_day + '"]').css('background', 'red');
        }
	$('.fc-other-month .fc-day-note').css('display', 'none');

	$('#calendar').fullCalendar({
		header: {
			right: 'prev,next', 
			center: '',
			left: 'title',
		},
		viewRender:function(view,element){
			if(dates.length>0){
				selected_day = $('#id_0-date').val().split(',');		
				console.log(selected_day) 
				for(var day=0; day<selected_day.length; day++){
					dates.push(selected_day[day]);
                			$('.fc-day[data-date="' + selected_day[day] + '"]').css('background', 'red');
        			}
			}
		},
		dayClick: function(date, jsEvent, view) {
			if(dates.indexOf(date.format("YYYY-MM-DD"))>-1){
				dates.splice(dates.indexOf(date.format("YYYY-MM-DD")),1)
				$('#id_0-date').val(dates.toString())
				$(this).css('background-color', 'white');
			}
			else{
				dates.push(date.format("YYYY-MM-DD"));
				$('#id_0-date').val(dates.toString())
				$(this).css('background-color', 'red');
			}
		}
	});
});
