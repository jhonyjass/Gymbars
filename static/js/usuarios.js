document.querySelector('form').addEventListener('submit', function (event) {
    const contraseñaInput = document.getElementById('contraseña');
    const errorMessage = contraseñaInput.nextElementSibling.nextElementSibling;

    const contraseña = contraseñaInput.value;
    const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])/;

    if (contraseña && !regex.test(contraseña)) {
        // Evitar enviar el formulario
        event.preventDefault();
        errorMessage.textContent = 'La contraseña debe contener al menos una letra mayúscula, un número y un carácter especial.';
        errorMessage.style.display = 'block';
        contraseñaInput.classList.add('is-invalid');
    } else {
        errorMessage.textContent = '';
        errorMessage.style.display = 'none';
        contraseñaInput.classList.remove('is-invalid');
    }
});
