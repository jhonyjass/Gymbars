from repositories.pagos_repo import PagosRepository
from repositories.suscrip_repo import SuscripcionesRepository
from models.suscripciones import *
from decimal import Decimal


class PagosService:

    @staticmethod
    def obtener_tipos_pagos():
        return PagosRepository.obtener_tipos_pagos()
    
    @staticmethod
    def obtener_pagos_cliente_año(id_cliente):
        return PagosRepository.obtener_pagos_por_cliente_año(id_cliente)
    

    @staticmethod
    def guardar_pago(data):
        try:
            mensualidad = SuscripcionesRepository.obtener_mensualidad_id(data['mensualidad'])
            if not mensualidad:
                return 'Mensualidad no encontrada'
            
            total_pagado = sum(pago.monto for pago in mensualidad.pagos)
            monto_decimal = Decimal(str(data['monto']))
            restante = mensualidad.cantidad - total_pagado

            if monto_decimal > restante:
                return 'El monto del pago excede el saldo pendiente'

            nuevo_pago = pagos(
                id_mensualidad=data['mensualidad'],
                fecha_pago=data['fecha_pago'],
                monto=monto_decimal,
                nota=data['nota'],
                id_tipo_pago=data['tipo_pago']
            )
            PagosRepository.guardar_pago(nuevo_pago)

            total_pagado += monto_decimal
            if total_pagado >= mensualidad.cantidad:
                mensualidad.estado_pago = True
                SuscripcionesRepository.actualizar_mensualidad(mensualidad)

            return True

        except Exception as e:
            print(f"Error en guardar_pago: {e}")
            return False


    @staticmethod
    def actualizar_pago(id_pago, data):
        try:
            pago = PagosRepository.obtener_pago_id(id_pago)
            if not pago:
                return 'Pago no encontrado'

            mensualidad = SuscripcionesRepository.obtener_mensualidad_id(pago.id_mensualidad)
            if not mensualidad:
                return 'Mensualidad no encontrada'

            # Calcular total pagado excluyendo el pago actual
            total_pagado = sum(p.monto for p in mensualidad.pagos if p.id_pago != pago.id_pago)

            # Verificar si el nuevo monto no excede lo que falta
            restante = mensualidad.cantidad - total_pagado
            if data['monto'] > restante:
                return 'El monto actualizado excede el saldo pendiente'

            # Actualizar campos del pago
            pago.fecha_pago = data['fecha_pago']
            pago.monto = data['monto']
            pago.nota = data['nota']
            pago.id_tipo_pago = data['tipo_pago']

            PagosRepository.actualizar_pago(pago)

            # Recalcular total con el nuevo monto incluido
            total_pagado += Decimal(str(data['monto']))

            # Verificar si ya esta completamente pagado
            mensualidad.estado_pago = total_pagado >= mensualidad.cantidad
            SuscripcionesRepository.actualizar_mensualidad(mensualidad)

            return True

        except Exception as e:
            print(f"Error en actualizar_pago: {e}")
            return False
