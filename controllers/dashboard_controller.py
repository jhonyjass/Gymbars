from flask import flash, render_template
from services.dashboard_service import DashboardService 
from services.reportes_service import ReporteService
from routes.rutas import dashboard_bp


@dashboard_bp.route('/')
def dashboard():

    ingresos_mensuales = ReporteService.obtener_ingresos_recibidos()
    porcentajes_tipos_pago = ReporteService.obtener_porcentajes_tipos_pago()
    conteo_suscripciones = ReporteService.obtener_suscrip_activas_inactivas()

    return render_template('dashboard/dashboard.html',
                           ingresos_mensuales =ingresos_mensuales,
                           porcentajes_tipos_pago = porcentajes_tipos_pago,
                           conteo_suscripciones = conteo_suscripciones)

