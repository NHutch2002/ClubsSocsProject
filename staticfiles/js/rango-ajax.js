$(document).ready(function() {
    $('#join_btn').click(function() {
        var societyIDVar;
        societyIDVar = $(this).attr('data-society');
        $.get('/Clubs&Socs/join_button/',
            {'society_id': societyIDVar},
            function(data) {
                $('#join_btn').text('Joined');
                $('#join_btn').attr("disabled", true);
                $('#join_btn').addClass("disabled")
            })
    });

    $('#event_btn').click(function() {
        var eventNameVar;
        eventNameVar = $(this).attr('data-event');
        $.get('/Clubs&Socs/event_button/',
            {'event_name': eventNameVar},
            function(data) {
                $('#event_btn').text('Attending');
                $('#event_btn').attr("disabled", true);
                $('#event_btn').addClass("disabled")
            })
    });
});