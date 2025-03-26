from flask import flash, render_template
from services.dashboard_service import DashboardService 
from routes.rutas import dashboard_bp


@dashboard_bp.route('/')
def dashboard():
    
    return render_template('dashboard/dashboard.html')

