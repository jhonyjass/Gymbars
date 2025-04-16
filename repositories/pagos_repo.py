from models.suscripciones import *
from datetime import datetime
from sqlalchemy import extract


class PagosRepository:
    
    @staticmethod
    def obtener_pago_id(id_pago):
        return conexion.session.query(pagos).filter_by(id_pago=id_pago).first()

    @staticmethod
    def obtener_tipos_pagos():
        return tipo_pagos.query.all()
    
    @staticmethod
    def obtener_pagos_por_cliente_año(id_cliente):
        año_actual = datetime.now().year
        return pagos.query \
            .join(mensualidades, pagos.id_mensualidad == mensualidades.id_mensualidad) \
            .join(suscripciones, mensualidades.id_suscripcion == suscripciones.id_suscripcion) \
            .filter(suscripciones.id_cliente == id_cliente) \
            .filter(extract('year', pagos.fecha_pago) == año_actual) \
            .order_by(pagos.id_pago) \
            .all()
    
    @staticmethod
    def guardar_pago(nuevo_pago):
        try:
            conexion.session.add(nuevo_pago)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al agregar {__class__.__name__}: {e}")
            raise e
        
    @staticmethod
    def actualizar_pago(pago):
        try:
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al actualizar {__class__.__name__}: {e}")
            raise e