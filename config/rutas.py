from flask import Blueprint

inicio = Blueprint('inicio', __name__, url_prefix='/')
dashboard = Blueprint('dashboard', __name__, url_prefix='/')





cerrar_sesion = Blueprint('cerrar_sesion',__name__,url_prefix='/cerrar_sesion')