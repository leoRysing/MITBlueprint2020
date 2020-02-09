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
        $.post('/sendemail', {
            message: message,
        }).done(function () {
            document.location.reload();
        });
    });
});