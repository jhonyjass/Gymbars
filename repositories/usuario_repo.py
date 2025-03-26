from flask import session
from models.usuarios import *


class UsuarioRepository:
    
    @staticmethod
    def usuario_actual():
       return session.get('usuario')

    @staticmethod
    def obtener_usuarios():
        return usuarios.query.all()
    
    @staticmethod
    def obtener_usuario_por_id(id_usuario):
        return usuarios.query.get(id_usuario)

    @staticmethod
    def obtener_usuario_por_usuario(usuario_ingresado):
        return usuarios.query.filter_by(usuario=usuario_ingresado).first()

    @staticmethod
    def obtener_tipo_usuario_por_id(id_tipo_usuario):
        return tipo_usuarios.query.get(id_tipo_usuario)
    
    @staticmethod
    def guardar_cambios_perfil(usuario):
        try:
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al agregar {__class__.__name__}: {e}")
            raise e 
