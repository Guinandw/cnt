    document.addEventListener("DOMContentLoaded", function () {
        // Obtener referencias a los elementos del formulario
        var tipoEventoSelect = document.getElementById("id_tipoEvento");
        var horaInicioInput = document.getElementById("id_horaInicio");
        var duracionSelect = document.getElementById("id_duracion");

        // Función para actualizar los campos según el tipo de evento seleccionado
        function actualizarCampos() {
            var tipoEvento = tipoEventoSelect.value;

            // Lógica para cambiar los campos según el tipo de evento
            if (tipoEvento === "GUARDIA MAÑANA") {
                // Cambiar la lógica según tus requisitos
                horaInicioInput.value = "07:00";
                duracionSelect.value = "8";
            } else if (tipoEvento === "GUARDIA TARDE") {
                horaInicioInput.value = "15:00";
                duracionSelect.value = "8";
            } else if (tipoEvento === "GUARDIA NOCHE") {
                horaInicioInput.value = "23:00";
                duracionSelect.value = "8";
                // Otras opciones...
            } else if (tipoEvento === "DISPONIBILIDAD") {
                horaInicioInput.value = "12:00";
                duracionSelect.value = "7";
            } else if (tipoEvento === "VACACIONES") {
                horaInicioInput.value = "00:00";
                duracionSelect.value = "24";
            }else if (tipoEvento === "FRANCO") {
                horaInicioInput.value = "00:00";
                duracionSelect.value = "24";
            }// Agregar más casos según sea necesario
        }

        // Escuchar el evento de cambio en el tipo de evento
        tipoEventoSelect.addEventListener("change", actualizarCampos);

        // Llamar a la función inicialmente para establecer los valores predeterminados
        actualizarCampos();
    });

