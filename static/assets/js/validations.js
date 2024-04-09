$('#errors-panel').hide();
$('#errors-panel').text('');

$('form').submit(function (e) {
    let username = $('#username').val();
    let password = $('#password').val();

    if (username.trim() === '' || password.trim() === '') {
        $('#errors-panel').text('Campos en blanco, complete todos los campos.');
        $('#errors-panel').show();
        e.preventDefault(); // Evitar que se envíe el formulario
    } else {
        $('#errors-panel').hide();
        $('#errors-panel').text('');
        showLoader();
    }
});

function showLoader() {
    $('#loader').css('display', 'block');
    $('#scraper_form').css('display', 'none');
}