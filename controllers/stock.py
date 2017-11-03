# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from compras.py")
def abm_categoria():
    grid = SQLFORM.grid(db.categoria)
    return locals()
def abm_marca():
    grid = SQLFORM.grid(db.marca)
    return locals()
def abm_color():
    grid = SQLFORM.grid(db.color)
    return locals()
def abm_talle():
    grid = SQLFORM.grid(db.talle)
    return locals()
def abm_producto():
    grid = SQLFORM.grid(db.producto)
    return {"grilla": grid}
def abm_cliente():
    return dict(message="abm_cliente")
def detalle_cliente():
    return dict(message="detalle_cliente")
    
def reporte_cliente():
    return dict(message="reporte_cliente")
def vista_previa():
    return dict(message="vista_previa")
def lista_cliente():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
def reporte_por_cliente():
    return dict(message="Reporde del producto")
def lista_ventas_por_cliente():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
def alta_producto():
    return dict (message="alta_producto")
def inventario_stock():
    return dict (message="inventario_stock")
