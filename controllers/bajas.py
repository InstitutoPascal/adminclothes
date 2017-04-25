# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from bajas.py")

def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id).delete()
    session.flash = "El cliente %s se borro exitosamente" % id
    # redirijo al usuario al listado
    redirect(URL(c="consultas", f="listado_clientes"))
def borrar_producto():
    # obtengo el primer argumento (ver URL)
    id = request.args[0]
    # busco y borro el registro
    db(db.producto.id == id).delete()
    session.flash = "El producto %s se borro exitosamente" % id
    # redirijo al usuario al listado
    redirect(URL(c="consultas", f="listado_productos"))
