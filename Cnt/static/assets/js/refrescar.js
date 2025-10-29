  function clicCada10Minutos() {
      setInterval(function () {
          var boton = document.getElementById("boton-inicio");
          if (boton) {
              boton.click(); // Simula el clic
              console.log("Clic en botón-inicio ejecutado");
          } else {
              console.warn("No se encontró el botón con id 'boton-inicio'");
          }
      }, 600000); // 10 minutos en milisegundos
  }

  window.onload = clicCada10Minutos;

