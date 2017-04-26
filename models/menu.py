# -*- coding: utf-8 -*-

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

response.google_analytics_id = None

response.menu = [(T('Home'), False, URL('default', 'index'), [])]  #Boton Home (vuelve a index)

DEVELOPMENT_MENU = True

if "auth" in locals():
    auth.wikimenu()
    
##Menu compras##
response.menu += [
                (T('Compras'), False, URL('default','index'), [
                    (T('ABM proveedor'), False, URL('altas', 'alta_cliente'),[]),
                    (T('Reporte subdiario'), False, URL('altas', 'alta_producto'),[]),
                    (T('Listado de proveedor'), False,URL('altas', 'alta_proveedor'),[]),
                    (T('Formulario de compra'), False, URL('altas', 'alta_vendedor'),[]),
                    (T('Orden de compra'), False, URL('altas', 'alta_empleado'),[])])]


### Menu Altas ###
response.menu += [
                (T('Stock'), False, URL('stock', 'index'), [
        (T('ABM Producto'), False, URL('stock', 'reporte_stock'), []),
        (T('reporte'), False, URL('stock', 'abm_producto'), []),

        (T('Emision de remito'), False, URL('stock', 'emision_remito'), []),
        (T('Recepcion de remito'), False, URL('stock', 'resepcion_remito'), [])])]


### Menu Consultas (parametros) ###
response.menu+=[(T('listados'),False,'#',
                     [(T('Cliente'),False,'#',
                       [(T('por Ciudad'),False,URL(request.application,'consultas','clientes_por_ciudad'),[]),
                        (T('por dni'),False,URL(request.application,'consultas','clientes_por_dni'),[])],),

                      (T('Productos'),False,'#',
                         [(T('por codigo'),False,URL(request.application,'consultas','productos_por_codigo'),[]),
                          (T('Precios de venta'),False,'#',
                            [(T('superiores'),False,URL(request.application,'consultas','productos_superiores_venta'),[]),
                             (T('inferiores'),False,URL(request.application,'consultas','productos_inferiores_venta'),[]),
                             (T('entre inferior y superior'),False,URL(request.application,'consultas','productos_entre_venta'),[])],),
                          (T('precios de compra'),False,'#',
                            [(T('superiores'),False,URL(request.application,'consultas','productos_superiores_compra'),[]),
                             (T('inferiores'),False,URL(request.application,'consultas','productos_inferiores_compra'),[]),
                             (T('entre inferior y superior'),False,URL(request.application,'consultas','productos_entre_compra'),[])],),
                          (T('por nombre'),False,'#',
                             [(T('uno'),False,URL(request.application,'consultas','productos_por_uno'),[]),
                              (T('varios'),False,URL(request.application,'consultas','productos_por_varios'),[]),
                            ],),],),

                      (T('proveedores'),False,'#',
                       [(T('por codigo'),False,URL(request.application,'consultas','proveedor_por_codigo'),[]),
                        (T('Por nombre'),False,URL(request.application,'consultas','proveedor_por_nombre'),[]),
                        (T('por ciudad'),False,URL(request.application,'consultas','proveedor_por_ciudad'),[]),],),
                     ],
                       )]
    
### Menu Registros Completos ###
response.menu.extend([
                    (T('Registros completos'), False, URL('default','index'), [
                    (T('Cliente'), False, URL('consultas', 'listado_Clientes'),[]),
                    (T('productos'), False, URL('consultas', 'listado_Productos'),[]),
                    (T('Proveedores'), False,URL('consultas', 'listado_Proveedor'),[]),
                    (T('Vendedores'), False, URL('consultas', 'listado_Vendedor'),[]),
                    (T('Ventas'), False, URL('consultas', 'listado_Ventas'),[])])])



"""if DEVELOPMENT_MENU:_()

if "auth" in locals(): auth.wikimenu()
if auth.has_membership(role='Gerente'):
    response.menu+=[(T('Altas'),False,'#',
               [(T('clientes'),False,URL(request.application,'altas','alta_clientes'),[]),
                 (T('empleados'),False,URL(request.application,'altas','alta_empleados'),[]),
                 (T('ventas'),False,URL(request.application,'altas','alta_vendedor'),[]),
                 (T('proveedores'),False,URL(request.application,'altas','alta_proveedor'),[]),
                 (T('productos'),False,URL(request.application,'altas','alta_producto'),[])],
                 )]
response.menu+=[(T('Consultas'),False,'#',
                 [(T('Clientes'),False,URL(request.application,'consultas','listado_clientes'),[]),
                 (T('Proveedores'),False,URL(request.application,'consultas','listado_proveedor'),[]),
                 (T('Articulos'),False,URL(request.application,'consultas','listado_productos'),[])],
                )]

response.menu+=[(T('Listado'),False,'#',
                 [(T('Clientes'),False,'#',
                   [(T('Por Ciudad'),False,URL(request.application,'listado','clientes_por_ciudad'),[]),
                    (T('Por DNI'),False,URL(request.application,'listado','clientes_por_dni'),[])],),
                  (T('Articulos'),False,'#',
                   [(T('Por Codigo'),False,URL(request.application,'listado','productos_por_codigo'),[]),
                    (T('Por Nombre'),False,URL(request.application,'listado','productos_por_codigo'),
                        [(T('UNO'),False,URL(request.application,'listado','productos_por_1_nombre'),[]),
                         (T('VARIOS'),False,URL(request.application,'listado','productos_por_varios_nombres'),[])])],),
                  (T('Proveedores'),False,'#',
                   [(T('Por Codigo'),False,URL(request.application,'listado','proveedor_por_codigo'),[]),
                    (T('Por Razon Social'),False,URL(request.application,'listado','proveedor_por_razon_social'),[]),
                    (T('Por Ciudad'),False,URL(request.application,'listado','proveedor_por_ciudad'),[]),],),
                 ],
                )]"""
