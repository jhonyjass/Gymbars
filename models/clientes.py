from app import conexion
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Integer, String, Boolean, Date




class clientes(conexion.Model):
    __tablename__ = 'clientes'

    id_cliente = conexion.Column(Integer, primary_key=True)
    nombre = conexion.Column(String(length=60))
    dpi = conexion.Column(Integer)
    fecha_nacimiento = conexion.Column(Date)
    edad = conexion.Column(Integer)
    sexo = conexion.Colum(Boolean)
    grupo_sanguineo = conexion.Column(String(length=50))
    cobertura_medica = conexion.Column(String(length=50))
    fecha_inscripccion = conexion.Column(Date)
    #Estado cliente Activo = 1 No 0
    estado = conexion.Column(bool,default=True)
    

class tipo_telefonos(conexion.Model):
    __tablename__ = 'tipo_telefonos'
    
    id_tipo_telefono = conexion.Column(Integer, primary_key=True)
    tipo_telefono = conexion.Column(String(length=20))


class telefonos(conexion.Model):
    __tablename__ = 'telefonos'

    id_telefono = conexion.Column(Integer, primary_key=True)
    id_cliente = conexion.Column(Integer, ForeignKey('clientes.id_clientes'))
    nombre_dueño = conexion.Column(String(length=50))
    telefono = conexion.Column(Integer)

















