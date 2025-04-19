from flask import g, session, redirect,url_for,render_template,flash
from functools import wraps


#Para poder verificar si es administrador
def administrador_requerido(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'usuario' in session and session['usuario']['tipo_usuario'] == 'Administrador':
            return func(*args, **kwargs)
        else:
            return render_template('alertas/restringir.html', alerta=True)
    return decorated_function