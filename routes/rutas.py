from flask import Blueprint

sesion_usuario_bp = Blueprint('sesion_usuario_bp', __name__, url_prefix='/')
usuarios_bp = Blueprint('usuarios_bp', __name__, url_prefix='/usuarios')
dashboard_bp = Blueprint('dashboard_bp', __name__, url_prefix='/dashboard')
clientes_bp = Blueprint('clientes_bp', __name__, url_prefix='/clientes')
