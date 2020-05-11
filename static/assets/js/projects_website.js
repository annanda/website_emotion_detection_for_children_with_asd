$(document).ready(function () {
    // alert('testing!');

    function make_request(name, email, message, method = "post") {
        $.ajax({
            url: '/save_forms',
            type: 'POST',
            data: JSON.stringify({
                name: name,
                email: email,
                message: message
            }),
            contentType: 'application/json',
            processData: false,
            success: function (msg) {
                // document.getElementById("behaviours").style.display = 'none';
                // document.getElementById("wrapper").style.display = 'block';
                //
                // document.getElementById('video_annotation').currentTime = time_seconds;
                // document.getElementById('video_annotation').play()
                alert('form submitted!')
            }
            // async: false
        });

    }


    $('#form_contact').on('click', function () {
        var name = $('input[name=name]').val();
        var email = $('input[name=email]').val();
        var message = $('input[name=message]').val()
        make_request(name, email, message);
    });


});