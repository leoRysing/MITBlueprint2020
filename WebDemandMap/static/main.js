// stuff
$(document).ready(function() {
    $('#register').click(function() {
        const Email = $('#Email').val();
        $.post('/register', {
            Email: Email,
        }).done(function () {
            document.location.reload();
        });
    });
    $('#logout').click(function() {
        $.post('/logout', {}).done(function() {
            document.location.reload();
        });
    });
    $('#request').click(function () {
        const message = $('#message').val();
        console.log("run")
        $.post('/sendemail', {
            message: message,
        }).done(function () {
            document.location.reload();
        });
    });
    $('#logout').click(function() {
        $.post('/logout', {}).done(function() {
            document.location.reload();
        });
    });
});

