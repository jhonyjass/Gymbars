from repositories.suscrip_repo import SuscripcionesRepository
from models.suscripciones import *
from datetime import date
from calendar import monthrange


class SuscripcionesService:

    @staticmethod
    def obtener_suscripciones():
        return SuscripcionesRepository.obtener_suscripciones_todas()
    
    @staticmethod
    def obtener_sus_activas():
        return SuscripcionesRepository.obtener_suscripciones_activas()
    
    @staticmethod
    def obtener_sus_inactivas():
        return SuscripcionesRepository.obtener_suscripciones_inactivas()
    
    @staticmethod
    def obtener_mensualidades_por_cliente(id_cliente):
        return SuscripcionesRepository.obtener_mensualidades_cliente(id_cliente)
    
    @staticmethod
    def obtener_mensualidades_año_cliente(id_cliente):
        return SuscripcionesRepository.obtener_mensualidades_cliente_año(id_cliente)

    @staticmethod
    def obtener_mensualidades_pediente_pago_cliente(id_cliente):
        return SuscripcionesRepository.obtener_mensualidades_cliente_pendiente_pago(id_cliente)
    
    @staticmethod
    def obtener_mensualidades_pagadas_cliente(id_cliente):
        return SuscripcionesRepository.obtener_mensualidades_cliente_pagadas(id_cliente)
    
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

        # Crear la mensualidad inicial
        SuscripcionesService.crear_mensualidad_inicial(nueva_suscripcion)

        return True

    @staticmethod
    def actualizar_suscripcion(data):
        suscripcion = SuscripcionesRepository.obtener_suscripcion_por_cliente(data['id_cliente'])

        if suscripcion:
            suscripcion.id_plan = data['plan']
            estado_anterior = suscripcion.estado_suscripcion
            suscripcion.estado_suscripcion = data.get('estado', True)

            SuscripcionesRepository.actualizar_suscripcion(suscripcion)

            # Si se reactivo
            if not estado_anterior and suscripcion.estado_suscripcion:
                # Validar que no exista mensualidad para esas fechas
                fecha_inicio = suscripcion.fecha_suscripcion
                año = fecha_inicio.year
                mes = fecha_inicio.month + 1
                if mes > 12:
                    mes = 1
                    año += 1

                try:
                    fecha_final = date(año, mes, fecha_inicio.day)
                except ValueError:
                    ultimo_dia = monthrange(año, mes)[1]
                    fecha_final = date(año, mes, ultimo_dia)

                if not SuscripcionesRepository.existe_mensualidad_para_fechas(
                    suscripcion.id_suscripcion,
                    fecha_inicio,
                    fecha_final
                ):
                    SuscripcionesService.crear_mensualidad_inicial(suscripcion)

            return True

        return False



    @staticmethod
    def crear_mensualidad_inicial(suscripcion):
        try:
            plan = SuscripcionesRepository.obtener_plan_id(suscripcion.id_plan)
            if not plan:
                raise Exception('No se encontró el plan')

            fecha_inicio = suscripcion.fecha_suscripcion
            año = fecha_inicio.year
            mes = fecha_inicio.month + 1

            if mes > 12:
                mes = 1
                año += 1

            # Calcular fecha final
            try:
                fecha_final = date(año, mes, fecha_inicio.day)
            except ValueError:
                ultimo_dia = monthrange(año, mes)[1]
                fecha_final = date(año, mes, ultimo_dia)

            nueva_mensualidad = mensualidades(
                id_suscripcion=suscripcion.id_suscripcion,
                fecha_inicio=fecha_inicio,
                fecha_final=fecha_final,
                estado_pago=False,
                cantidad=plan.precio
            )

            SuscripcionesRepository.guardar_mensualidad(nueva_mensualidad)

        except Exception as e:
            print(f"Error al crear mensualidad inicial: {e}")