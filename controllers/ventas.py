# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from ventas.py")
def abm_clientes():
    grid = SQLFORM.grid(db.cliente)
    return {"grilla": grid}
def abm_ventas():
    return dict(message="abm_ventas")
def detalle_ventas():
    return dict(message="detalle_ventas")
    
def reporte_ventas():
    return dict(message="reporte_ventas")
def vista_previa():
    return dict(message="vista_previa")
def lista_ventas():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
def reporte_por_cliente():
    return dict(message="Reporde de las ventas segun Cliente")
def lista_ventas_por_cliente():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
def alta_cliente():

    return dict (message="alta_cliente")
