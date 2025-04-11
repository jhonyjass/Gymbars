from models.suscripciones import *

class SuscripcionesRepository:
    
    @staticmethod
    def obtner_planes():
        return planes.query.all()
    
    @staticmethod
    def obtener_suscripcion_por_cliente(id_cliente):
        return suscripciones.query.filter_by(id_cliente = id_cliente).first()
    
    @staticmethod
    def guardar_suscripcion(suscripcion):
        try:
            conexion.session.add(suscripcion)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al agregar {__class__.__name__}: {e}")
            raise e
    
    @staticmethod
    def actualizar_suscripcion(suscripcion):
        try:
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al actualizar {__class__.__name__}: {e}")
            raise e
