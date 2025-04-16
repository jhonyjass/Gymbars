from models.suscripciones import *
from datetime import datetime
from sqlalchemy import extract, func


class SuscripcionesRepository:

    @staticmethod
    def obtener_suscripciones_todas():
        return suscripciones.query.all()
    
    @staticmethod 
    def obtener_suscripciones_activas():
        return suscripciones.query.filter_by(estado_suscripcion = True).all()
    
    @staticmethod
    def obtener_suscripciones_inactivas():
        return suscripciones.query.filter_by(estado_suscripcion = False).all()
    
    @staticmethod
    def obtener_mensualidad_id(id_mensualidad):
        return mensualidades.query.get(id_mensualidad)
    
    @staticmethod
    def obtener_mensualidades_cliente(id_cliente):
        return mensualidades.query.join(suscripciones).filter(suscripciones.id_cliente == id_cliente).all()
    
    @staticmethod
    def obtener_mensualidades_cliente_año(id_cliente):
        año_actual = datetime.now().year
        return mensualidades.query \
            .join(suscripciones, mensualidades.id_suscripcion == suscripciones.id_suscripcion) \
            .filter(suscripciones.id_cliente == id_cliente) \
            .filter(extract('year', mensualidades.fecha_inicio) == año_actual) \
            .outerjoin(pagos, pagos.id_mensualidad == mensualidades.id_mensualidad) \
            .add_columns(func.coalesce(func.sum(pagos.monto), 0).label('total_pagado')) \
            .group_by(mensualidades.id_mensualidad) \
            .all()

    @staticmethod
    def obtener_mensualidades_cliente_pagadas(id_cliente):
        return mensualidades.query \
            .join(suscripciones) \
            .filter(suscripciones.id_cliente == id_cliente) \
            .filter((mensualidades.estado_pago) == True) \
            .order_by(mensualidades.id_mensualidad) \
            .all()

    @staticmethod
    def obtener_mensualidades_cliente_pendiente_pago(id_cliente):
        return mensualidades.query \
            .join(suscripciones) \
            .filter(suscripciones.id_cliente == id_cliente) \
            .filter((mensualidades.estado_pago) == False) \
            .order_by(mensualidades.id_mensualidad) \
            .all()
    

    
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

    @staticmethod
    def actualizar_mensualidad(mensualidad):
        try:
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al actualizar {__class__.__name__}: {e}")
            raise e
        
    @staticmethod
    def guardar_mensualidad(mensualidad):
        try:
            conexion.session.add(mensualidad)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al actualizar {__class__.__name__}: {e}")
            raise e
        