from models.clientes import *
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

class ClientesRepository:
    
    @staticmethod
    def listado_clientes():
        return clientes.query.order_by(desc(clientes.id_cliente)).all()
    
    @staticmethod
    def obtener_clientes():
        return clientes.query.all()
    
    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        return clientes.query.get_or_404(id_cliente)
    
    @staticmethod
    def obtener_info_cliente(id_cliente):
        return clientes.query.options(
            joinedload(clientes.telefonos), 
            joinedload(clientes.afecciones),
            joinedload(clientes.direcciones),
            joinedload(clientes.medidas),
            joinedload(clientes.suscripciones)
        ).filter_by(id_cliente = id_cliente).first()

    @staticmethod
    def objetivos_para_cliente():
        return objetivos.query.all()
    
    
    @staticmethod
    def agregar_cliente(cliente):
        ClientesRepository.transaccion_cliente(cliente)

    @staticmethod
    def agregar_telefonos_cliente(telefono):
        ClientesRepository.transaccion_cliente(telefono)

    @staticmethod
    def agregar_direcciones_cliente(direccion):
        ClientesRepository.transaccion_cliente(direccion)

    @staticmethod
    def agregar_afecciones_cliente(afeccion):
        ClientesRepository.transaccion_cliente(afeccion)

    @staticmethod
    def transaccion_cliente(objeto):
        """ Agregar el objeto cliente """
        try:
            conexion.session.add(objeto)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al agregar {objeto.__class__.__name__}: {e}")
            raise e 
    
    @staticmethod
    def agregar_medidas_cliente(medidas):
        try:
            conexion.session.add(medidas)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al agregar {__class__.__name__}: {e}")
            raise e
        


    @staticmethod
    def obtener_telefono_por_id(id_telefono):
        return telefonos.query.filter_by(id_telefono=id_telefono).first()

    @staticmethod
    def actualizar_telefono(telefono):
        try:
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al actualizar teléfono: {e}")
            raise e
        
    @staticmethod
    def eliminar_telefono(telefono):
        try:
            conexion.session.delete(telefono)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            print(f"Error al eliminar teléfono: {e}")
            raise e