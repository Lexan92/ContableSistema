/*function transformarEnEditable(nodo){
//El nodo recibido es SPAN
if (editando == false) {
var nodoTd = nodo.parentNode; //Nodo TD
var nodoTr = nodoTd.parentNode; //Nodo TR
var nodoContenedorForm = document.getElementById('contenedorForm'); //Nodo DIV
var nodosEnTr = nodoTr.getElementsByTagName('td');
var codigo = nodosEnTr[0].textContent; var nombre = nodosEnTr[1].textContent;
var dependecia = nodosEnTr[2].textContent; var grado = nodosEnTr[3].textContent;
var rubro = nodosEnTr[4].textContent; var opciones = nodosEnTr[5].textContent;
var nuevoCodigoHtml = '<td><input type="text" name="codigo" id="codigo" value="'+codigo+'" size="20"></td>'+
'<td><input type="text" name="nombre" id="nombre" value="'+nombre+'" size="20"</td>'+
'<td><input type="text" name="dependencia" id="dependecia" value="'+dependecia+'" size="20"</td>'+
'<td><input type="text" name="grado" id="grado" value="'+grado+'" size="10"</td>'+
'<td><input type="text" name="rubro" id="rubro" value="'+rubro+'" size="20"</td> <td>En edición</td>';
 
nodoTr.innerHTML = nuevoCodigoHtml;
 
nodoContenedorForm.innerHTML = 'Pulse Aceptar para guardar los cambios o cancelar para anularlos'+
'<form name = "formulario" action="http://aprenderaprogramar.com" method="get" onsubmit="capturarEnvio()" onreset="anular()">'+
'<input class="boton" type = "submit" value="Aceptar"> <input class="boton" type="reset" value="Cancelar">';
editando = "true";}
else {alert ('Solo se puede editar una línea. Recargue la página para poder editar otra');
}
}
 
function capturarEnvio(){
var nodoContenedorForm = document.getElementById('contenedorForm'); //Nodo DIV
nodoContenedorForm.innerHTML = 'Pulse Aceptar para guardar los cambios o cancelar para anularlos'+
'<form name = "formulario" method="get" onsubmit="capturarEnvio()" onreset="anular()">'+
'<input type="hidden" name="codigo" value="'+document.querySelector('#codigo').value+'">'+
'<input type="hidden" name="nombre" value="'+document.querySelector('#nombre').value+'">'+
'<input type="hidden" name="dependencia" value="'+document.querySelector('#dependencia').value+'">'+
'<input type="hidden" name="grado" value="'+document.querySelector('#grado').value+'">'+
'<input type="hidden" name="rubro" value="'+document.querySelector('#rubro').value+'">'+
'<input class="boton" type = "submit" value="Aceptar"> <input class="boton" type="reset" value="Cancelar">';
document.formulario.submit();
}
 
function anular(){
window.location.reload();
}*/
var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

$('.table-add').click(function () {
  var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
  $TABLE.find('table').append($clone);
});

$('.table-remove').click(function () {
  $(this).parents('tr').detach();
});

$('.table-up').click(function () {
  var $row = $(this).parents('tr');
  if ($row.index() === 1) return; // Don't go above the header
  $row.prev().before($row.get(0));
});

$('.table-down').click(function () {
  var $row = $(this).parents('tr');
  $row.next().after($row.get(0));
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.click(function () {
  var $rows = $TABLE.find('tr:not(:hidden)');
  var headers = [];
  var data = [];
  
  // Get the headers (add special header logic here)
  $($rows.shift()).find('th:not(:empty)').each(function () {
    headers.push($(this).text().toLowerCase());
  });
  
  // Turn all existing rows into a loopable array
  $rows.each(function () {
    var $td = $(this).find('td');
    var h = {};
    
    // Use the headers from earlier to name our hash keys
    headers.forEach(function (header, i) {
      h[header] = $td.eq(i).text();   
    });
    
    data.push(h);
  });
  
  // Output the result
  $EXPORT.text(JSON.stringify(data));
});