// stuff
$(document).ready(function() {
    $('#register').click(function() {
        const email = $('#email').val();
        console.log(email);
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
    $('#request').click(function () {
        const email = $('#email').val();
        console.log("got here")
        const message = $('#message').val();
        /*const geotag = $localStorage.getItem("marker");*/
        const geotag = "12.345, 67.8910"
        console.log("got here two")
        console.log("run")
        $.post('/submit', {
            email: email,
            message: message,
            geotag: geotag,
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

