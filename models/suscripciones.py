from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Integer, String, Boolean,Numeric,Date
from conexion import conexion



class planes(conexion.Model):
    __tablename__ = 'planes'

    id_plan = conexion.Column(Integer, primary_key=True)
    nombre = conexion.Column(String(length=30))
    precio = conexion.Column(Numeric(precision=10, scale=2))
    descripcion = conexion.Column(String(length=50))

    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion



class suscripciones(conexion.Model):
    __tablename__ = 'suscripciones'

    id_suscripcion = conexion.Column(Integer, primary_key=True)
    id_plan = conexion.Column(Integer, ForeignKey('planes.id_plan'))
    id_cliente = conexion.Column(Integer, ForeignKey('clientes.id_cliente'))
    estado_suscripcion = conexion.Column(Boolean)
    fecha_suscripcion = conexion.Column(Date)

    plan_cliente = relationship('planes', backref=backref('suscripciones', cascade='all, delete-orphan'))
    sub_cliente = relationship('clientes', backref=backref('suscripciones', cascade='all, delete-orphan'))

    def __init__(self, id_plan, id_cliente, estado_suscripcion, fecha_suscripcion ):
        self.id_plan = id_plan
        self.id_cliente = id_cliente
        self.estado_suscripcion = estado_suscripcion
        self.fecha_suscripcion = fecha_suscripcion 



class mensualidades(conexion.Model):
    __tablename__ = 'mensualidades'

    id_mensualidad = conexion.Column(Integer, primary_key=True)
    id_suscripcion = conexion.Column(Integer, ForeignKey('suscripciones.id_suscripcion'))
    fecha_inicio = conexion.Column(Date)
    fecha_final = conexion.Column(Date)
    estado_pago = conexion.Column(Boolean)
    cantidad = conexion.Column(Numeric(precision=10, scale=2))

    suscrip = relationship('suscripciones', backref=backref('mensualidades', cascade='all, delete-orphan'))

    def __init__(self, id_suscripcion, fecha_inicio, fecha_final, estado_pago, cantidad):
        self.id_suscripcion = id_suscripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.estado_pago = estado_pago
        self.cantidad = cantidad



class tipo_pagos(conexion.Model):
    __tablename__ = 'tipo_pagos'

    id_tipo_pago = conexion.Column(Integer, primary_key=True)
    nombre = conexion.Column(String(length=30))

    def __init__(self, nombre):
        self.nombre = nombre



class pagos(conexion.Model):
    __tablename__ = 'pagos'
    id_pago = conexion.Column(Integer, primary_key=True)
    id_mensualidad = conexion.Column(Integer, ForeignKey('mensualidades.id_mensualidad'))
    fecha_pago = conexion.Column(Date)
    monto = conexion.Column(Numeric(precision=10, scale=2))
    nota = conexion.Column(String(length=100))
    id_tipo_pago = conexion.Column(Integer, ForeignKey('tipo_pagos.id_tipo_pago'))

    mensualidad = relationship('mensualidades', backref=backref('pagos', cascade='all, delete-orphan'))
    tipo_pago = relationship('tipo_pagos', backref=backref('pagos', cascade='all, delete-orphan'))

    def __init__(self, id_mensualidad, fecha_pago, monto, nota, id_tipo_pago):
        self.id_mensualidad = id_mensualidad
        self.fecha_pago = fecha_pago
        self.monto = monto
        self.nota = nota
        self.id_tipo_pago = id_tipo_pago