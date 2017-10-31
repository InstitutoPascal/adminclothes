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
if auth.has_membership('Admin'):
    response.menu += [
                    (T('Compras'), False, URL('default','index'), [
                        (T('ABM proveedor'), False, URL('compras', 'abm_proveedor'),[]),
                        (T('Facturas'), False, URL('compras', 'abm_producto'),[])])]
                    


### Menu stock ###
if auth.has_membership('Admin'):
    response.menu += [
                (T('Stock'), False, URL('stock', 'index'), [
        (T('ABM Producto'), False, URL('stock', 'abm_producto'), []),
        (T('ABM Categoria'), False, URL('stock', 'abm_categoria'), []),
        (T('ABM Color'), False, URL('stock', 'abm_color'), []),
        (T('ABM Talle'), False, URL('stock', 'abm_talle'), []),
        (T('ABM Marca'), False, URL('stock', 'abm_marca'), []),        
        (T('Inventario'), False, URL('stock', 'inventario_stock'), [])])]



    
### Menu ventas ###
if auth.has_membership('Admin'):
    response.menu.extend([
                    (T('Ventas'), False, URL('default','index'), [
                    (T('Clientes'), False, URL('ventas', 'abm_clientes'),[]),
                    (T('Ingreso de pagos'), False, URL('ventas', 'ingreso_pagos'),[]),
                    (T('Reporte de ventas'), False,URL('ventas', 'reporte_ventas'),[]),
                    (T('Reportes de ventas por clientes'), False, URL('ventas', 'reporte_por_cliente'),[]),
                    (T('Reporte de pagos'), False, URL('ventas', 'listado_pagos'),[])])])
### Menu indumentaria ###
categoria= db(db.categoria).select()
tupla = []
for c in categoria:
    tupla.append((T(str(c.nombre).lower().capitalize()), False, URL('indumentaria', 'categoria',args=c.id),[]))
response.menu.extend([
                    (T('Indumentaria'), False, URL('default','index'), tupla)])



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
