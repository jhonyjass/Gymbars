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





/*-------------------------------------Contador caracteres-----------------------------------*/
function setupCharacterLimit(inputElement) {
    inputElement.addEventListener('input', function () {
        var maxLength = this.getAttribute('maxlength');
        var currentLength = this.value.length;
        var errorMsg = this.parentElement.querySelector('.error-message');

        // Verifica si el texto supera el limite
        if (currentLength >= maxLength) {
            this.classList.add('is-invalid'); 
            errorMsg.style.display = 'block';
            errorMsg.textContent = 'No puedes ingresar más de ' + maxLength + ' caracteres.';
        } else {
            this.classList.remove('is-invalid');
            errorMsg.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    // Seleccionamos todos los inputs con maxlength y aplicamos la funcion
    document.querySelectorAll('input[maxlength], textarea[maxlength]').forEach(function (input) {
        setupCharacterLimit(input);
    });

    // Verifica si existe un formulario antes de acceder a el
    var form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (event) {
            if (form.querySelector('.is-invalid')) {
                event.preventDefault();
                event.stopPropagation();
            }
        });
    }
});
/*-------------------------------------Fin Contador caracteres-----------------------------------*/



/*-------------------Funcion para poder mandar url del obejeto a eliminar ---------------------------------------------- */

document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los botones de eliminar
    const eliminarBtns = document.querySelectorAll('.eliminar-btn');

    eliminarBtns.forEach(btn => {
        // Agregar un listener de clic a cada boton
        btn.addEventListener('click', function () {
            // Obtener la URL de eliminar
            const actionUrl = btn.getAttribute('data-action-url');
            // Obtener el enlace de eliminacion
            const eliminarLink = document.querySelector('#eliminarLink');
            // Actualizar el atributo href del enlace de eliminar en el modal
            eliminarLink.setAttribute('href', actionUrl);
        });
    });
});

/*-------------------Funcion para poder mandar url del obejeto a eliminar ---------------------------------------------- */
