

/* CODIGO PARA LA PAGINA CARGAR SEMANA */
/* PARTE ENCARGADA DE AGREGAR UN ELEMENTO HTML PARA PODER INGRESAR UN FERIADO EN CASO DE HABERLO. */
  document.addEventListener("DOMContentLoaded", () => {
    const addFeriadoButton = document.getElementById("addFeriado");
    const contenedorFeriados = document.getElementById("contenedorFeriados");
  
    addFeriadoButton.addEventListener("click", () => {

    const nuevoElemento = document.createElement("div");

    nuevoElemento.className = "col-lg-6 mb-3";

    var label = document.createElement("label");

    label.htmlFor = "agregarFeriado";
    label.innerHTML = "Fecha Feriado";


    var inputGroup = document.createElement("div");

    inputGroup.className = "input-group";

    var inputGroupText = document.createElement("div");

    inputGroupText.className = "input-group-text bg-primary-transparent text-primary";

    var icon = document.createElement("i");

    icon.className = "fe fe-calendar text-20";
    inputGroupText.appendChild(icon);
    var input = document.createElement("input");
    input.className = "form-control";
    input.id = "agregarFeriado";
    input.placeholder = "DD/MM/YYYY";
    input.type = "date";
    input.name = "feriados";
    input.required = false;
    inputGroup.appendChild(inputGroupText);
    inputGroup.appendChild(input);
    nuevoElemento.appendChild(label);
    nuevoElemento.appendChild(inputGroup);

    // Agregar el nuevo elemento al contenedor de feriados
    var contenedorFeriados = document.getElementById("contenedorFeriados");
    contenedorFeriados.appendChild(nuevoElemento);
     
    });


});




  