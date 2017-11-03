# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    """db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])"""
    db = DAL('sqlite://storage.db')
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------


auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
##Tabla Clientes##
db.define_table('cliente',
                 db.Field('dni','integer'),
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('sexo'),
                 db.Field('localidad'),
                 db.Field('calle','string'),
                 db.Field('numero_calle','integer'),
                 db.Field('telefono','integer'))

db.cliente.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.cliente.dni.requires=IS_NOT_IN_DB(db, db.cliente.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000'),
db.cliente.sexo.requires=IS_IN_SET(['Masculino','Femenino'], zero=T('Selecciona sexo'))
db.cliente.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.cliente.localidad.requires=IS_IN_SET(['20 de Junio', 'Gregorio de Laferrere', 'Ramos Mejía', 'Aldo Bonzi', 'Isidro Casanova', 'San Justo', 'Ciudad Evita', 'La Tablada', 'Tapiales', 'Ciudad Madero', 'Lomas del Mirador', 'Villa Luzuriaga', 'Gonzáles Catán', 'Rafael Castillo', 'Virrey del Pino'], zero=T('Selecciona localidad'))

# --------------------------------------------------------------------------------------

##Tabla Proveedor##
db.define_table('proveedor',
                 db.Field('nombre_empresa','string'),
                 db.Field('localidad','string'),
                 db.Field('calle','string'),
                 db.Field('numero_calle','integer'),
                 db.Field('telefono','integer'),
                 db.Field('email','string'))
db.proveedor.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.proveedor.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.email.requires=IS_EMAIL(error_message='¡El mail no es válido!'), IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.proveedor.nombre_empresa.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.calle.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.numero_calle.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')

# --------------------------------------------------------------------------------------
db.define_table('color',
                db.Field('nombre_color','string',label='Nombre')
               )
db.define_table('talle',
                db.Field('nombre_talle','string',label='Nombre')
               )
db.define_table('marca',
                db.Field('nombre_marca','string',label='Nombre'),
                db.Field('logo','upload')
               )
db.define_table('categoria',
                db.Field('nombre','string')
                )
##Tabla Producto##
db.define_table('producto',
                db.Field('nombre','string'),
                db.Field('descripcion','string'),
                db.Field('genero','integer',requires=IS_IN_SET({"1":"Masculino","2":"Femenino"},zero="Seleccionar...",error_message='Seleccione el genero')),
                db.Field('impuesto','integer',requires= IS_IN_SET({"1":"10.5%","2":"21%","3":"27%"},zero='Seleccionar...',error_message='Seleccione el impuesto')),
                db.Field('color',db.color,requires= IS_IN_DB(db, 'color.id', db.color.nombre_color,zero='Seleccionar...',error_message='Seleccione el color')),
                db.Field('marca',db.marca,requires= IS_IN_DB(db, 'marca.id', db.marca.nombre_marca,zero='Seleccionar...',error_message='Seleccione la marca')),
                db.Field('talle',db.talle,requires= IS_IN_DB(db, 'talle.id', db.talle.nombre_talle,zero='Seleccionar...',error_message='Seleccione el talle')),
                #db.Field('precio_compra','integer'),
                db.Field('precio_venta','integer'),
                db.Field('categoria',db.categoria,requires= IS_IN_DB(db, 'categoria.id', db.categoria.nombre,zero='Seleccionar...',error_message='Seleccione la categoria')),
                #db.Field('proveedor','string'),
                db.Field('imagen', 'upload'))




db.producto.descripcion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
#db.producto.precio_compra.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(5, error_message='Solo hasta 5 caracteres')
db.producto.precio_venta.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(5, error_message='Solo hasta 5 caracteres')
#db.producto.stock.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
#----------------------------------------------------------------------------------------------------------------

##Tabla Vendedor##
db.define_table('vendedor',
                db.Field('dni','integer'),
                db.Field('nombre','string'),
                db.Field('apellido','string'),
                db.Field('password','password'))
db.vendedor.dni.requires=IS_NOT_IN_DB(db, db.vendedor.dni, error_message = 'El DNI ingresado  ya se encuentra registrado'), IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.vendedor.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.vendedor.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.vendedor.password.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_ALPHANUMERIC(error_message='No se permiten simbolos y espacios'), IS_LENGTH(8, error_message='Solo hasta 8 caracteres')

#CREO LA TABLA EMPLEADOS#
db.define_table('empleados',
              db.Field('dni','integer'),
              db.Field('apellido','string'),
              db.Field('nombre','string'),
              db.Field('password','password'))
db.empleados.dni.requires=IS_NOT_IN_DB(db, db.empleados.dni, error_message = 'El DNI ingresado  ya se encuentra registrado'), IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.empleados.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.empleados.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.empleados.password.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_ALPHANUMERIC(error_message='No se permiten simbolos y espacios'), IS_LENGTH(8, error_message='Solo hasta 8 caracteres')

# --------------------------------------------------------------------------------------

##Tabla Ventas##
db.define_table('ventas',
                db.Field('vendedor',db.vendedor),
                db.Field('cliente',db.cliente),
                db.Field('articulo_a_comprar',db.producto),
                db.Field('fecha_venta','date'),
                db.Field('numero_factura', 'integer'),
                db.Field('cantidad','integer'),
                db.Field('total','integer'))

db.ventas.vendedor.requires=IS_IN_DB(db,db.vendedor.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione vendedor'))
db.ventas.cliente.requires=IS_IN_DB(db,db.cliente.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione cliente'))
db.ventas.articulo_a_comprar.requires=IS_IN_DB(db,db.producto.id,'%(articulo_a_comprar)s',zero=T('Seleccione producto'))
db.ventas.fecha_venta.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%m/%Y')
db.ventas.cantidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.ventas.total.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(5, error_message='Solo hasta 5 caracteres')

#-----------------------------------------------------------------------------------------------------------------------------------
