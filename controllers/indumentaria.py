# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from indumentaria.py")
def index():
    regs = db(db.producto.id>0).select()
    return dict(producto=regs)
def categoria():
    genero_sel = None
    marca_sel = None
    color_sel = None
    talle_sel = None
    try:
        genero_sel =  int(request.post_vars["genero"]) if request.post_vars["genero"] is not None else None 
    except:
        pass
    try:
        talle_sel =  int(request.post_vars["talle"]) if request.post_vars["talle"] is not None else None 
    except:
        pass
    try:
        color_sel =  int(request.post_vars["color"]) if request.post_vars["color"] is not None else None 
    except:
        pass
    try:
        marca_sel =  int(request.post_vars["marca"]) if request.post_vars["marca"] is not None else None 
    except:
        pass
    criterio = db.producto.categoria==request.args(0)
    if genero_sel is not None:
        criterio &= db.producto.genero == genero_sel
    if talle_sel is not None:
        criterio &= db.producto.talle == talle_sel
    if marca_sel is not None:
        criterio &= db.producto.marca == marca_sel
    if color_sel is not None:
        criterio &= db.producto.color == color_sel
    productos=db(criterio).select()
    color=db(db.color).select()
    marca=db(db.marca).select()
    talle=db(db.talle).select()
    genero =[]
    genero.append({"nombre":"Femenino","id":1})
    genero.append({"nombre":"Masculino","id":2})
             
   
    return locals()

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
