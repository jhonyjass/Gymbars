from models.clientes import *
from models.suscripciones import *
from datetime import date
from sqlalchemy import extract, func, case



class ReportesRepository:


    @staticmethod
    def ingresos_por_mes():
        resultados = conexion.session.query(
            extract('year', pagos.fecha_pago).label('año'),
            extract('month', pagos.fecha_pago).label('mes'),
            func.coalesce(func.sum(pagos.monto), 0).label('total')
        ).group_by(
            extract('year', pagos.fecha_pago),
            extract('month', pagos.fecha_pago)
        ).order_by(
            extract('year', pagos.fecha_pago),
            extract('month', pagos.fecha_pago)
        ).all()

        return [
            {"año": int(r.año), "mes": int(r.mes), "total": float(r.total)}
            for r in resultados
        ]

    @staticmethod
    def porcentaje_por_tipo_pago():
        total_general = conexion.session.query(func.coalesce(func.sum(pagos.monto), 0)).scalar()

        resultados = conexion.session.query(
            tipo_pagos.nombre.label('tipo_pago'),
            func.sum(pagos.monto).label('total'),
            (func.sum(pagos.monto) / total_general * 100).label('porcentaje')
        ).join(tipo_pagos, pagos.id_tipo_pago == tipo_pagos.id_tipo_pago
        ).group_by(tipo_pagos.nombre
        ).all()

        return [
            {
                "tipo_pago": r.tipo_pago,
                "total": float(r.total),
                "porcentaje": round(float(r.porcentaje), 2)
            }
            for r in resultados
        ]
    
    @staticmethod
    def contar_suscripciones_estado():
        resultado = conexion.session.query(
            func.sum(case((suscripciones.estado_suscripcion == True, 1), else_=0)).label('activas'),
            func.sum(case((suscripciones.estado_suscripcion == False, 1), else_=0)).label('inactivas')
        ).one()

        return {
            "activas": int(resultado.activas),
            "inactivas": int(resultado.inactivas)
        }
    

    @staticmethod
    def obtener_clientes_con_pagos_pendientes():
        return (
            conexion.session.query(
                clientes.id_cliente,
                clientes.nombre,
                clientes.correo,
                mensualidades.fecha_inicio,
                mensualidades.fecha_final,
                mensualidades.cantidad,
            )
            .join(suscripciones, clientes.id_cliente == suscripciones.id_cliente)
            .join(mensualidades, suscripciones.id_suscripcion == mensualidades.id_suscripcion)
            .filter(mensualidades.estado_pago == False)
            .order_by(clientes.id_cliente, mensualidades.fecha_inicio)
            .all()
        )
    
    @staticmethod
    def obtener_ingresos_del_dia():
        hoy = date.today()
        return (
            conexion.session.query(
                clientes.nombre.label('nombre_cliente'),
                clientes.correo,
                pagos.monto,
                pagos.fecha_pago,
                tipo_pagos.nombre.label('tipo_pago')
            )
            .join(mensualidades, mensualidades.id_mensualidad == pagos.id_mensualidad)
            .join(suscripciones, suscripciones.id_suscripcion == mensualidades.id_suscripcion)
            .join(clientes, clientes.id_cliente == suscripciones.id_cliente)
            .join(tipo_pagos, tipo_pagos.id_tipo_pago == pagos.id_tipo_pago)
            .filter(pagos.fecha_pago == hoy)
            .order_by(pagos.fecha_pago)
            .all()
        )
    
    @staticmethod
    def obtener_ingresos_por_mes_año(mes, año):
        return (
            conexion.session.query(
                clientes.nombre.label('nombre_cliente'),
                clientes.correo,
                pagos.monto,
                pagos.fecha_pago,
                tipo_pagos.nombre.label('tipo_pago')
            )
            .join(mensualidades, mensualidades.id_mensualidad == pagos.id_mensualidad)
            .join(suscripciones, suscripciones.id_suscripcion == mensualidades.id_suscripcion)
            .join(clientes, clientes.id_cliente == suscripciones.id_cliente)
            .join(tipo_pagos, tipo_pagos.id_tipo_pago == pagos.id_tipo_pago)
            .filter(extract('month', pagos.fecha_pago) == mes)
            .filter(extract('year', pagos.fecha_pago) == año)
            .order_by(pagos.fecha_pago)
            .all()
        )
    

