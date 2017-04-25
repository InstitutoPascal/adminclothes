# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")

@auth.requires_login()
def listado_clientes():
    datosClientes = db().select(db.cliente.ALL)
    i=0
    tablafinal=[]
    for x in datosClientes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Codigo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Sexo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Número de calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Teléfono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' Clientes',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.sexo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosClientes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)
#-----------------------------------------------------------------
@auth.requires_login()
def listado_productos():
    datosProductos = db(db.producto.proveedor == db.proveedor.id).select(db.producto.ALL, db.proveedor.nombre_empresa)
    i=0
    tablafinal=[]
    for x in datosProductos:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Equipo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Descripción',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Código de barras',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Precio de compra',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Precio de venta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Stock',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Proveedor',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Producto',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.producto.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.producto.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.codigo_barra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.precio_compra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.stock,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.proveedor.nombre_empresa,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosProductos]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)
#----------------------------------------------------------------------------------
@auth.requires_login()
def listado_proveedor():
    datosProductos = db(db.producto.proveedor == db.proveedor.id).select(db.producto.ALL, db.proveedor.nombre_empresa)
    i=0
    tablafinal=[]
    for x in datosProductos:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Equipo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Descripción',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Código de barras',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Precio de compra',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Precio de venta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Stock',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Proveedor',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Producto',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.producto.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.producto.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.codigo_barra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.precio_compra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.stock,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.proveedor.nombre_empresa,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosProductos]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)
#-------------------------------------------------------------------------------
def listado_vendedor():
    datosVendedor = db().select(db.vendedor.ALL)
    i=0
    tablafinal=[]
    for x in datosVendedor:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:100px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Contraseña',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Vendedores',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.password,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosVendedor]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)
#-------------------------------------------------------------------------------
def listado_ventas():
    datosVentas = db((db.ventas.vendedor==db.vendedor.id)&(db.ventas.cliente==db.clientes.id)&(db.ventas.equipo==db.producto.id)).select(db.ventas.ALL ,db.vendedor.nombre, db.vendedor.apellido, db.clientes.nombre, db.clientes.apellido, db.producto.equipo)
    i=0
    tablafinal=[]
    for x in datosVentas:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Vendedor',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Cliente',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Equipo',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Fecha de venta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Número de factura',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Cantidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Total',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Ventas',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.ventas.id,_style='width:100px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.vendedor.nombre, ' ', x.vendedor.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.clientes.nombre, ' ', x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.fecha_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.numero_factura,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.cantidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.total,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosVentas]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)
