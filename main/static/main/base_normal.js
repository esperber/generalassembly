$(document).ready(function() {
        $('li').hover(function(){
                $(this).addClass('active');
        }, function(){
                $(this).removeClass('active');
        });
        $('#calendar').fullCalendar({
        // put your options and callbacks here
        })
});

