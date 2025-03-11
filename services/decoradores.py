from flask import g, session, redirect,url_for,render_template,flash
from functools import wraps



#Decorador para verificar la sesion del usuario
def verifica_sesion(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('inicio.iniciar_sesion'))
        return f(*args, **kwargs)
    return decorated_function





#Para poder verificar si es administrador
def administrador_requerido(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'usuario' in session and session['usuario']['tipo_usuario'] == 'Administrador':
            return func(*args, **kwargs)
        else:
            return render_template('alertas/permisos.html', alerta=True)
    return decorated_function