from flask import session, redirect, url_for, render_template, current_app as app
from config.rutas import cerrar_sesion


#Funcion para cerrar sesion
@cerrar_sesion.route('/', methods=['GET'])
def cerrar_session():
    session.pop('usuario', None)
    return redirect(url_for('inicio.iniciar_sesion'))



#Funcion para mostrar error 404 
def pagina_no_encontrada(e):
    return render_template('alertas/404.html',error_404=True),404