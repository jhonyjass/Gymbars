from flask import render_template, request, redirect, url_for, flash, session, g
from config.rutas import dashboard
from services.decoradores import *
# from controllers.dashboard.datos import *
# from controllers.dashboard.reportes import *



@dashboard.route('/dashboard')
@verifica_sesion
# @administrador_requerido
def dashboards():

    

    return render_template('dashboard/dashboard.html')