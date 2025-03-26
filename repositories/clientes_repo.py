from models.clientes import *
from sqlalchemy import desc

class ClientesRepository:
    
    @staticmethod
    def listado_clientes():
        return clientes.query.order_by(desc(clientes.id_cliente)).all()
    
    @staticmethod
    def obtener_clientes():
        return clientes.query.all()
    
    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        return clientes.query.get(id_cliente)
    
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