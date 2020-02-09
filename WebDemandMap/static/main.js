// stuff
$(document).ready(function() {
    $('#register').click(function() {
        const email = $('#email').val();
        $.post('/register', {
            email: email,
        }).done(function () {
            document.location.reload();
        });
    });
    $('#logout').click(function() {
        $.post('/logout', {}).done(function() {
            document.location.reload();
        });
    });
    $('#submit').click(function () {
        const message = $('#message').val();
        $.post('/message', {
            message: message,
        }).done(function () {
            document.location.reload();
        });
    });
});