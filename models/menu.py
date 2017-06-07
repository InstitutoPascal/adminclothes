# -*- coding: utf-8 -*-

response.logo = A(B('Adminclothes'), XML('&trade;&nbsp;'),
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


### Menu stock ###
response.menu += [
                (T('Stock'), False, URL('stock', 'index'), [
        (T('ABM Producto'), False, URL('stock', 'reporte_stock'), []),
        (T('reporte'), False, URL('stock', 'abm_producto'), []),

        (T('Emision de remito'), False, URL('stock', 'emision_remito'), []),
        (T('Recepcion de remito'), False, URL('stock', 'resepcion_remito'), [])])]



    
### Menu ventas ###
response.menu.extend([
                    (T('Ventas'), False, URL('default','index'), [
                    (T('Clientes'), False, URL('ventas', 'abm_clientes'),[]),
                    (T('Facturas'), False, URL('ventas', 'abm_ventas'),[]),
                    (T('Reporte de ventas'), False,URL('consultas', 'listado_Proveedor'),[]),
                    (T('Reportes de ventas por clientes'), False, URL('consultas', 'listado_Vendedor'),[]),
                    (T('Nota de credito'), False, URL('consultas', 'listado_Ventas'),[])])])
### Menu indumentaria ###
response.menu.extend([
                    (T('Indumentaria'), False, URL('default','index'), [
                    (T('Remeras'), False, URL('indumentaria', 'remeras'),[]),
                    (T('Camisas'), False, URL('indumentaria', 'camisas'),[]),
                    (T('jeans'), False,URL('indumentaria', 'jeans'),[]),
                    (T('Bermudas y shorts'), False, URL('indumentaria', 'bermudas'),[]),
                    (T('Abrigos'), False, URL('indumentaria', 'abrigos'),[])])])



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
