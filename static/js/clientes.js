document.addEventListener("DOMContentLoaded", function () {
    const addPhoneButton = document.getElementById("add-phone-button");
    const phoneContainer = document.getElementById("phone-container");

    let phoneCount = 0;

    // Funcion para agregar un telefono
    function addPhone() {
        phoneCount++;

        // Crear un contenedor para telefonos
        const phoneDiv = document.createElement("div");
        phoneDiv.classList.add("row", "mt-3");
        phoneDiv.id = `phone-${phoneCount}`;

        phoneDiv.innerHTML = `
            <div class="col-md-6 mt-3">
                <label for="telefono_${phoneCount}" class="form-label">Teléfono</label>
                <input type="number" class="form-control" id="telefono_${phoneCount}" name="telefono_${phoneCount}" maxlength="10" required>
                <div class="error-message text-danger" style="display: none;"></div>
            </div>

            <div class="col-md-4 mt-3">
                <label for="tipo_tel_${phoneCount}" class="form-label">Tipo de teléfono</label>
                <select class="form-select" aria-label="Default select example" id="tipo_tel_${phoneCount}" name="tipo_tel_${phoneCount}" required>
                    <option value="" selected disabled>Tipo de teléfono</option>
                    <option value="Personal">Personal</option>
                    <option value="Pareja">Pareja</option>
                    <option value="Familiar">Familiar</option>
                    <option value="Amigo">Amigo</option>
                </select>
            </div>

            <div class="col-md-2 d-flex align-items-end">
                <button type="button" class="btn remove-button text-danger" onclick="removePhone('${phoneDiv.id}')" style="${phoneCount === 1 ? 'display: none;' : ''}">
                    <i class="bi bi-trash3 me-1"></i>
                    Eliminar
                </button>
            </div>
        `;

        phoneContainer.appendChild(phoneDiv);

        setupCharacterLimit(phoneDiv.querySelector(`#telefono_${phoneCount}`));
    }

    // Agregar el primer telefono por defecto
    addPhone();

    // Agregar mas telefonos
    addPhoneButton.addEventListener("click", addPhone);
});

// Funcion para eliminar un telefono
function removePhone(phoneId) {
    const phoneDiv = document.getElementById(phoneId);
    if (phoneDiv) {
        phoneDiv.remove();
    }
}