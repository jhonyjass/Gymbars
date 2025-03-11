/*---------------------------- Validad formularios -----------------------------------------*/

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()

/*----------------------------Fin Validad formularios -----------------------------------------*/



/*-------------------- Mostrar contraseña de formulario -------------------------------------*/

$(document).ready(function () {
    $('#togglePassword').click(function () {
        var passwordInput = $('#contraseña');

        if (passwordInput.attr('type') === 'password') {
            passwordInput.attr('type', 'text');
            $('#togglePassword').removeClass('bi-eye-slash-fill').addClass('bi-eye-fill');
        } else {
            passwordInput.attr('type', 'password');
            $('#togglePassword').removeClass('bi-eye-fill').addClass('bi-eye-slash-fill');
        }
    });
});

/*----------------- fin Mostrar contraseña de formulario -------------------------------------*/





/*--------------------Alerta flotante mensajes -------------------------------------------*/

// Cerrar alerta en 5 segundos
document.addEventListener('DOMContentLoaded', function(){
    setTimeout(function() {
        var alert = document.querySelector('.alert-sonner');
        if (alert) {
            alert.classList.remove('show');
        }
    }, 5000);
});

// Alerta flotante 
document.addEventListener('scroll', function () {
    const alert = document.querySelector('.alert-sonner');
    if (alert) {
        // Obtiene la posicion relativa del scroll
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        // Ajusta la posicion de la alerta segun el scroll
        alert.style.top = `${30 + scrollTop}px`;
    }
});

/*--------------------Fin Alerta flotante mensajes -------------------------------------------*/

