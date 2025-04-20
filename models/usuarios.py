from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Integer, String
from conexion import conexion
import bcrypt



class tipo_usuarios(conexion.Model):
    __tablename__ = 'tipo_usuarios'

    id_tipo_usuario = conexion.Column(Integer, primary_key=True)
    tipo_usuario = conexion.Column(String(length=50))

    def __init__(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario


class usuarios(conexion.Model):
    __tablename__ = 'usuarios'

    id_usuario = conexion.Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_usuario = conexion.Column(Integer,ForeignKey('tipo_usuarios.id_tipo_usuario'))
    nombre = conexion.Column(String(length=30))
    usuario = conexion.Column(String(length=30))
    contraseña = conexion.Column(String(length=60))
    
    #Relacion a modelo tipo de usuario 
    tipo_usuario = relationship('tipo_usuarios', backref=backref('usuarios', cascade='all, delete-orphan'))


    def __init__(self, id_tipo_usuario,nombre,usuario,contraseña):
        self.id_tipo_usuario = id_tipo_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.set_contraseña(contraseña)
        

    def set_contraseña(self, contraseña):
        #Generar un hash de la contraseña usando bcrypt
        hashed = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
        #Almacenar el hash
        self.contraseña = hashed.decode('utf-8')

    def verificar_contraseña(self, contraseña):
        #Verificar si la contraseña proporcionada coincide con la almacenada en la base de datos
        return bcrypt.checkpw(contraseña.encode('utf-8'), self.contraseña.encode('utf-8'))
