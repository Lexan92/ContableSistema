var editando = false;

function transformarEnEditable(nodo) {
    //El nodo recibido es SPAN
    if (editando == false) {
        var nodoTd = nodo.parentNode; //Nodo TD
        var nodoTr = nodoTd.parentNode; //Nodo TR
        var nodoContenedorForm = document.getElementById('contenedorForm'); //Nodo DIV
        var nodosEnTr = nodoTr.getElementsByTagName('td');
        var codigo = nodosEnTr[0].textContent; var cuentas = nodosEnTr[1].textContent;
        var debe = nodosEnTr[2].textContent; var haber = nodosEnTr[3].textContent;
         var opciones = nodosEnTr[4].textContent;
        var nuevoCodigoHtml = '<td><input type="text" name="codigo" id="codigo" value="' + codigo + '" size="5"></td>' +
            '<td><input type="text" name="cuentas" id="cuentas" value="' + cuentas + '" size="15"</td>'+
            '<td><input type="text" name="debe" id="debe" value="' + debe + '" size="10"></td>'+
            '<td><input type="text" name="haber" id="haber" value="' + haber + '" size="10"></td><td>En edición</td>';

        nodoTr.innerHTML = nuevoCodigoHtml;

        nodoContenedorForm.innerHTML = 'Pulse Aceptar para guardar los cambios o cancelar para anularlos' +
            '<form name = "formulario"  method="get" onsubmit="capturarEnvio()" onreset="anular()">' +
            '<input class="boton" type = "submit" value="Aceptar"> <input class="boton" type="reset" value="Cancelar">';
        editando = "true";
    }
    else {
        alert('Solo se puede editar una línea. Recargue la página para poder editar otra');
    }
}

function capturarEnvio() {
    var nodoContenedorForm = document.getElementById('contenedorForm'); //Nodo DIV
    nodoContenedorForm.innerHTML = 'Pulse Aceptar para guardar los cambios o cancelar para anularlos' +
        '<form name = "formulario" method="get" onsubmit="capturarEnvio()" onreset="anular()">' +
        '<input type="hidden" name="codigo" value="' + document.querySelector('#codigo').value + '">' +
        '<input type="hidden" name="cuentas" value="' + document.querySelector('#cuentas').value + '">' +
        '<input type="hidden" name="debe" value="' + document.querySelector('#debe').value + '">' +
        '<input type="hidden" name="haber" value="' + document.querySelector('#haber').value + '">' +
        '<input class="boton" type = "submit" value="Aceptar"> <input class="boton" type="reset" value="Cancelar">';
    document.formulario.submit();
}

function anular() {
    window.location.reload();
}