
//           $('#consulta').click(function(){
//             $("#contenido").load('{% url 'queryCatalogo' %}');
//             // $("#contenido").load('/conta/Catalogo');
//                          });
// function consultarCat(){
//     document.getElementById("contenido").load('{% url 'queryCatalogo' %}');
//     // $("#contenido").load('{% url 'queryCatalogo' %}');
//        // $("#contenido").load('/conta/Catalogo');
// }                     

function putnewcod(codPadre,codNextSon){
  // var nextson = document.getElementById(cns);
  // nextson.value = codPadre+codNextSon;
  // document.getElementById(cns)=nextson;
  document.getElementById(cns).value=codPadre+codNextSon;

}
 function addRow(tableID)
      {
               var table = document.getElementById(tableID);
               var rowCount = table.rows.length;
               var row = table.insertRow(rowCount);
               //se crea una varible celda y .type define q tipo sera
               var cell1 = row.insertCell(0);
               var element1 = document.createElement("input");
               element1.type = "checkbox";
               cell1.appendChild(element1);


               var lista = document.getElementById("insertcodigo");
                 // Obtener el índice de la opción que se ha seleccionado
                var indiceSeleccionado = lista.selectedIndex;
                // Con el índice y el array "options", obtener la opción seleccionada
                var opcionSeleccionada = lista.options[indiceSeleccionado];
                  // Obtener el valor y el texto de la opción seleccionada
                var textoSeleccionado = opcionSeleccionada.text;
                var valorSeleccionado = opcionSeleccionada.value;
                // alert("Opción seleccionada: " + textoSeleccionado + "\n Valor de la opción: " + valorSeleccionado);
              
               var cell2 = row.insertCell(1);
               var element2 = document.createElement("input");
               element2.type = "text";
               element2.value = textoSeleccionado;
               element2.name = "nom";
               document.getElementById("insertcodigo").value="";
               cell2.appendChild(element2);

               var cell3 = row.insertCell(2);
               var element3 = document.createElement("input");
               // hidden
               element3.type = "hidden";
               element3.name = "cod";
               element3.value = valorSeleccionado;
               // document.getElementById("insertnombre").value="";
                 cell3.appendChild(element3);

               var cell4 = row.insertCell(3);
               var element4 = document.createElement("input");
               element4.type = "number";
               element4.min = "0.00";
               element4.step="any";
               element4.name = "debe";
               element4.value = document.getElementById("insertdebe").value;
               document.getElementById("insertdebe").value="";
               cell4.appendChild(element4);

               var cell5 = row.insertCell(4);
               var element5 = document.createElement("input");
               element5.type = "number";
               element5.min = "0.00";
               element5.step="any";
               element5.name = "haber";
               element5.value = document.getElementById("inserthaber").value;
               document.getElementById("inserthaber").value="";
               cell5.appendChild(element5);

              //  var lista = document.getElementById("insertcodigo");
 
              //   // Obtener el índice de la opción que se ha seleccionado
              // var indiceSeleccionado = lista.selectedIndex;
              // // Con el índice y el array "options", obtener la opción seleccionada
              // var opcionSeleccionada = lista.options[indiceSeleccionado];
 
              // // Obtener el valor y el texto de la opción seleccionada
              // var textoSeleccionado = opcionSeleccionada.text;
              // var valorSeleccionado = opcionSeleccionada.value;
              // alert("Opción seleccionada: " + textoSeleccionado + "\n Valor de la opción: " + valorSeleccionado);


      }
function deleteRow(tableID)
      {
          try {
               var table = document.getElementById(tableID);
               var rowCount = table.rows.length;
               for(var i=0; i<rowCount; i++)
                  {
                    var row = table.rows[i];
                    var chkbox = row.cells[0].childNodes[0];
                    if(null != chkbox && true == chkbox.checked) 
                    {
                         table.deleteRow(i);
                         rowCount--;
                         i--;
                    }
                  }

               }catch(e) {alert(e);}
      }