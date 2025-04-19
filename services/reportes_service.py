from repositories.reportes_repo import ReportesRepository
from collections import defaultdict


class ReporteService:


    @staticmethod
    def obtener_ingresos_recibidos():
        return ReportesRepository.ingresos_por_mes()

    @staticmethod
    def obtener_porcentajes_tipos_pago():
        return ReportesRepository.porcentaje_por_tipo_pago()
    
    @staticmethod
    def obtener_suscrip_activas_inactivas():
        return ReportesRepository.contar_suscripciones_estado()
    
    @staticmethod
    def obtener_clientes_deudores():
        datos = ReportesRepository.obtener_clientes_con_pagos_pendientes()

        clientes_deuda = defaultdict(lambda: {
            'nombre': '',
            'correo': '',
            'mensualidades': [],
            'total': 0
        })

        for id_cliente, nombre, correo, fecha_inicio, fecha_final, cantidad in datos:
            cliente = clientes_deuda[id_cliente]
            cliente['nombre'] = nombre
            cliente['correo'] = correo
            cliente['mensualidades'].append({
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'cantidad': float(cantidad)
            })
            cliente['total'] += float(cantidad)

        return clientes_deuda.values()
    
    @staticmethod
    def obtener_ingresos_diarios():
        return ReportesRepository.obtener_ingresos_del_dia()

    @staticmethod
    def obtener_ingresos_por_mes_año_seleccionado(mes, año):
        ingresos_data = ReportesRepository.obtener_ingresos_por_mes_año(mes, año)
        nombres_meses = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
        }
        nombre_mes = nombres_meses.get(mes, 'Mes Inválido')
        return {
            'ingresos': ingresos_data,
            'nombre_mes': nombre_mes,
            'año': año
        }