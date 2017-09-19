# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from indumentaria.py")
def index():
    regs = db(db.producto.id>0).select()
    return dict(producto=regs)

def ver():
    # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
    # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.producto.id==prod_id).select().first()
    return dict(producto=reg)

def mostrar():
    # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
    # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.producto.id==prod_id).select(db.producto.imagen).first()
    # obtenemos la imagen (nombre de archivo completo, stream=flujo de datos=archivo abierto -open-):
    (filename, stream) = db.producto.imagen.retrieve(reg.imagen)
    # obtenemos extension original para determinar tipo de contenido:
    import os.path
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".jpg", ".jpeg", ".face"):
        formato = "image/jpeg"
    elif ext in (".png"):
        formato = "image/png"
    response.headers['Content-Type'] = formato
    # devolver al navegador el contenido de la imagen
    return stream
def remeras():
    return dict(message="remeras")
def camisas():
    return dict(message="camisas")
def jeans():
    return dict(message="jeans")
def bermudas():
    return dict(message="bermudas")
def abrigos():
    return dict(message="abrigos")
def detalle_venta():
    return dict(message="detalle_venta")
def datos_facturacion():
    return dict(message="datos_facturacion")
def fin_compra():
    return dict(message="fin_compra")
def cupon_de_pago():
    return dict(message="cupon_de_pago")
