from flask import Flask
from flask_migrate import Migrate
from configuraciones import Configuraciones
from utils.utils import *
from conexion import conexion


# Iniciar flask 
app = Flask(__name__)
app.config.from_object(Configuraciones)

# Instancia base de datos
conexion.init_app(app)

# Verificar conexion base de datos
with app.app_context():
    try:
        print("La conexion a la base de datos es correctamente.")
    except Exception as e:
        print("Error al conectar a la base de datos:", str(e))


# Actualizar modelos
migrate = Migrate(app, conexion)


# Llamar modelos
from models.usuarios import *
from models.clientes import *


# Crear modelos 
with app.app_context():
    conexion.create_all()


# Llamar los controladores
from controllers.sesion_usuario_controller import sesion_usuario_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.clientes_controller import clientes_bp


# Registro de los blueprints 
app.register_blueprint(sesion_usuario_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(clientes_bp)


# Bloquear vistas sin sesion
@app.before_request
def verificar_sesion_middleware():
    redir = verificar_sesion() 
    if redir:
        return redir 


# Registro del manejador de errores 404
app.register_error_handler(404, pagina_no_encontrada)
