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
