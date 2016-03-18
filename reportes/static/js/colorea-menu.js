var path=window.location.pathname.split('/');
var palabra=path[2];

switch (palabra) {
  case "inventario":{
    $("#item-inventario").addClass("active");
    $("#item-articulos").addClass("active");
    break;
  }
  case "categorias":{
    $("#item-inventario").addClass("active");
    $("#item-categorias").addClass("active");
    break;
  }
  case "categoria":{
    $("#item-inventario").addClass("active");
    $("#item-categorias").addClass("active");
    break;
  }
  case "descuentos":{
    $("#item-inventario").addClass("active");
    $("#item-descuentos").addClass("active");
    break;
  }
  case "descuento":{
    $("#item-inventario").addClass("active");
    $("#item-descuentos").addClass("active");
    break;
  }
  case "proveedores":{
    $("#item-inventario").addClass("active");
    $("#item-proveedores").addClass("active");
    break;
  }
  case "proveedor":{
    $("#item-inventario").addClass("active");
    $("#item-proveedores").addClass("active");
    break;
  }
  case "ventas":{
    $("#item-ventas").addClass("active");
    break;
  }
  case "compras":{
    $("#item-compras").addClass("active");
    break;
  }
  case "gastos":{
    $("#item-gastos").addClass("active");
    $("#item-gasto").addClass("active");
    break;
  }
  case "gasto":{
    $("#item-gastos").addClass("active");
    $("#item-gasto").addClass("active");
    break;
  }
  case "tipo_gastos":{
    $("#item-gastos").addClass("active");
    $("#item-tipo_gastos").addClass("active");
    break;
  }
  case "tipo_gasto":{
    $("#item-gastos").addClass("active");
    $("#item-tipo_gastos").addClass("active");
    break;
  }
  case "empleados":{
    $("#item-empleados").addClass("active");
    break;
  }
  case "clientes":{
    $("#item-clientes").addClass("active");
    break;
  }
  case "ventas_credito":{
    $("#item-clientes").addClass("active");
    break;
  }
  case "abonos":{
    $("#item-clientes").addClass("active");
    break;
  }
  case "reporte_general":{
    $("#item-reportes").addClass("active");
    $("#item-reporte_general").addClass("active");
    break;
  }
  case "mi_cuenta":{
    $("#item-perfil").addClass("active");
    break;
  }
  case "paquetes":{
    $("#item-paquetes").addClass("active");
    break;
  }
}
