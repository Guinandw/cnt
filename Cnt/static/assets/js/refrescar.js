// Función para recargar la página en cada cambio de hora
function refrescarEnCambioDeHora() {
    // Obtener la fecha actual
    var fechaActual = new Date();
    
    // Calcular el tiempo restante hasta el próximo cambio de hora
    var tiempoRestanteHastaProximoCambioDeHora = (60 - fechaActual.getMinutes()) * 60 * 1000 - fechaActual.getSeconds() * 1000; // Tiempo restante hasta el próximo cambio de hora en milisegundos
    
    // Establecer el tiempo de espera antes de recargar la página
    setTimeout(function() {
      location.reload();
    }, tiempoRestanteHastaProximoCambioDeHora);
  }
  
  // Llamar a la función para recargar en cada cambio de hora
  refrescarEnCambioDeHora();