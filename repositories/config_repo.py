from models.usuarios import *

class ConfigRepository():

    @staticmethod
    def obtener_tipos_usuario():
        return tipo_usuarios.query.all()
    
    @staticmethod
    def obtener_usuarios():
        return usuarios.query.all()
    
    @staticmethod
    def obtener_usuarios_excluyendo_session(id_usuario):
        return usuarios.query.filter(usuarios.id_usuario != id_usuario).all()

    
    @staticmethod
    def usuario_existe(nombre_usuario):
        return conexion.session.query(usuarios).filter_by(usuario=nombre_usuario).first()

    @staticmethod
    def agregar_usuario(usuario):
        try:
            conexion.session.add(usuario)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al guardar usuario: {e}")
            raise e
        
    @staticmethod
    def eliminar_usuario(id_usuario):
        try:
            usuario = conexion.session.query(usuarios).get(id_usuario)
            
            if usuario:
                conexion.session.delete(usuario)
                conexion.session.commit()
                return True
            
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al eliminar usuario: {e}")
            return False
