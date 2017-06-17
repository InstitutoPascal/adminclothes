# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from compras.py")
def abm_proveedor():
    grid = SQLFORM.grid(db.proveedor)
    return {"grilla": grid}
def abm_producto():
    return dict(message="abm_producto")
def detalle_producto():
    return dict(message="detalle_producto")
    
def reporte_producto():
    return dict(message="reporte_producto")
def vista_previa():
    return dict(message="vista_previa")
def lista_producto():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
def reporte_por_producto():
    return dict(message="Reporde del producto")
def lista_ventas_por_producto():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
