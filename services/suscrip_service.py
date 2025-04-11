from repositories.suscrip_repo import SuscripcionesRepository
from models.suscripciones import *


class SuscripcionesService:
    
    @staticmethod
    def obtener_planes():
        return SuscripcionesRepository.obtner_planes()
    
    @staticmethod
    def cliente_tiene_suscripcion(id_cliente):
        return SuscripcionesRepository.obtener_suscripcion_por_cliente(id_cliente) is not None
    
    @staticmethod
    def obtener_suscripcion_cliente(id_cliente):
        return SuscripcionesRepository.obtener_suscripcion_por_cliente(id_cliente)

    @staticmethod
    def crear_suscripcion(data):
        # Verificar si ya existe una suscripción para el cliente
        suscripcion_existente = SuscripcionesRepository.obtener_suscripcion_por_cliente(data['id_cliente'])

        if suscripcion_existente:
            return 'El cliente ya tiene una suscripción activa.'

        nueva_suscripcion = suscripciones(
            id_cliente = data['id_cliente'],
            id_plan = data['plan'],
            estado_suscripcion = data['estado'],
            fecha_suscripcion = data['fecha_suscripcion']
        )

        SuscripcionesRepository.guardar_suscripcion(nueva_suscripcion)

        return True

    @staticmethod
    def actualizar_suscripcion(data):
        suscripcion = SuscripcionesRepository.obtener_suscripcion_por_cliente(data['id_cliente'])

        if suscripcion:
            suscripcion.id_plan = data['plan']
            suscripcion.estado_suscripcion = data.get('estado', True)
            SuscripcionesRepository.actualizar_suscripcion(suscripcion)
            return True

        return False
