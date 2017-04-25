# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from altas.py")

#alta_cliente
@auth.requires_login()
def alta_cliente():
    form = SQLFORM(db.cliente)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_proveedor
@auth.requires_membership(role='Administrador')
def alta_proveedor():
    form = SQLFORM(db.proveedor)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_producto
@auth.requires_membership(role='Administrador')
def alta_producto():
    form = SQLFORM(db.producto)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_ventas
@auth.requires_login()
def alta_ventas():
    form = SQLFORM(db.ventas)
    if form.accepts(request.vars, session):
        redirect(URL('alta_ventas'))
        response.flash = 'El formulario fue aceptado'
        if form.accepts(request.vars, session):
            redirect(URL('alta_ventas'))
     
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)


#alta_vendedor
@auth.requires_membership(role='Administrador')
def alta_vendedor():
    form = SQLFORM(db.vendedor)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_empleado
@auth.requires_login()
def alta_empleado():
    form = SQLFORM(db.empleados)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)
