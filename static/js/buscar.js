$("#busqueda").keyup(function(){
    consulta.search($(this).val()).draw();
})

var consulta = $("#searchTable").DataTable();


