function changeTab(event, tabId) {
    // Obtener todos los elementos con la clase "tab-pane"
    var tabContent = document.getElementsByClassName('tab-pane');

    // Iterar sobre los elementos y ocultarlos
    for (var i = 0; i < tabContent.length; i++) {
        tabContent[i].classList.remove('active');
    }

    // Mostrar el contenido de la pestaña seleccionada
    document.getElementById(tabId).classList.add('active');
}

document.querySelectorAll('.filters__button').forEach(button => {
    button.addEventListener('click', function () {
        // Eliminar la clase 'active' de todos los botones
        document.querySelectorAll('.filters__button').forEach(btn => btn.classList.remove('active'));

        // Añadir la clase 'active' al botón seleccionado
        this.classList.add('active');
    });
});


(() => {
    'use strict'

    const getStoredTheme = () => localStorage.getItem('theme') || 'light';  // Si no hay tema guardado, por defecto será 'light'
    const setStoredTheme = theme => localStorage.setItem('theme', theme);

    const setTheme = theme => {
        if (theme === 'auto') {
            document.documentElement.setAttribute('data-bs-theme', (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme);
        }
    };

    const toggleTheme = () => {
        const currentTheme = getStoredTheme();
        const newTheme = (currentTheme === 'dark') ? 'light' : 'dark';  // Alternar entre 'dark' y 'light'

        setStoredTheme(newTheme);
        setTheme(newTheme);

        // Alternar la visibilidad de los iconos
        const iconoMoon = document.getElementById('iconoMoon');
        const iconoSun = document.getElementById('iconoSun');

        if (newTheme === 'dark') {
            iconoMoon.classList.remove('d-none');
            iconoSun.classList.add('d-none');
        } else {
            iconoMoon.classList.add('d-none');
            iconoSun.classList.remove('d-none');
        }
    };

    // Establecer el tema al cargar la página según la preferencia almacenada
    const storedTheme = getStoredTheme();
    setTheme(storedTheme);  // Aplica el tema que está guardado en localStorage

    // Cambiar tema si el usuario cambia su preferencia en el sistema (ej. cambiar de modo oscuro a claro)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        const storedTheme = getStoredTheme();
        setTheme(storedTheme);  // Asegura que se mantenga el tema guardado al cambiar el modo del sistema
    });

    window.addEventListener('DOMContentLoaded', () => {
        const temaButton = document.getElementById('temaButton');
    
        if (temaButton) {  // Verifica si el botón existe en la vista actual
            temaButton.addEventListener('click', toggleTheme);
            
            // Inicializar la visibilidad de los iconos de acuerdo al tema guardado
            const iconoMoon = document.getElementById('iconoMoon');
            const iconoSun = document.getElementById('iconoSun');
    
            if (iconoMoon && iconoSun) {  // Verifica que los iconos existen
                if (getStoredTheme() === 'dark') {
                    iconoMoon.classList.remove('d-none');
                    iconoSun.classList.add('d-none');
                } else {
                    iconoMoon.classList.add('d-none');
                    iconoSun.classList.remove('d-none');
                }
            }
        }
    });
    
})();

