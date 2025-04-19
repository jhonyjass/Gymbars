from flask import flash, render_template, redirect, url_for, request
from services.dashboard_service import DashboardService 
from services.reportes_service import ReporteService
from routes.rutas import dashboard_bp
from utils.pdf_config import *



@dashboard_bp.route('/')
def dashboard():

    ingresos_mensuales = ReporteService.obtener_ingresos_recibidos()
    porcentajes_tipos_pago = ReporteService.obtener_porcentajes_tipos_pago()
    conteo_suscripciones = ReporteService.obtener_suscrip_activas_inactivas()

    return render_template('dashboard/dashboard.html',
                           ingresos_mensuales =ingresos_mensuales,
                           porcentajes_tipos_pago = porcentajes_tipos_pago,
                           conteo_suscripciones = conteo_suscripciones)



@dashboard_bp.route('/reportes', methods = ['GET', 'POST'])
def reportes():

    return render_template('dashboard/lista_reportes.html')



@dashboard_bp.route('/clientes_pendiente_pago', methods = ['GET','POST'])
def clientes_pendiente_pago():
    try:
        datos_clientes = ReporteService.obtener_clientes_deudores()
        return generar_reporte(
                        'reportes/clientes_pendiente_pago.html',
                        nombre_archivo = 'Clientes pendiente de pago',
                        datos_clientes = datos_clientes)
    except Exception as e:
        print(e)
        flash('Error al generar el reporte.', 'error')
    return redirect(url_for('dashboard_bp.reportes'))



@dashboard_bp.route('/ingresos_del_dia', methods = ['GET','POST'])
def ingresos_del_dia():
    try:
        ingresos = ReporteService.obtener_ingresos_diarios()
        return generar_reporte(
                        'reportes/ingresos_del_dia.html',
                        nombre_archivo = 'Ingresos diarios',
                        ingresos = ingresos)
    except Exception as e:
        print(e)
        flash('Error al generar el reporte.', 'error')
    return redirect(url_for('dashboard_bp.reportes'))



@dashboard_bp.route('/reporte_ingresos_mes_año', methods=['GET', 'POST'])
def reporte_ingresos_mes_año():
    if request.method == 'POST':
        mes = int(request.form.get('mes'))
        año = int(request.form.get('año'))
        try:
            ingresos = ReporteService.obtener_ingresos_por_mes_año_seleccionado(mes, año)
            return generar_reporte(
                'reportes/reporte_ingresos_mes_año.html',
                nombre_archivo=f'Reporte de ingresos de {ingresos["nombre_mes"]} de {ingresos["año"]}',
                ingresos=ingresos['ingresos'],
                nombre_mes=ingresos['nombre_mes'],
                año=ingresos['año']
            )
        except Exception as e:
            print(e)
            flash('Error al generar el reporte.', 'error')
            return redirect(url_for('dashboard_bp.reportes'))

    return render_template('reportes/seleccionar_mes.html')
