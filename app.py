from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config
from services.utilidades import *
from config.rutas import *
import conexion


#Iniciar flask 
app = Flask(__name__)

#Clave secreta
app.secret_key = config('SECRET_KEY')


#Conexion base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
conexion = SQLAlchemy(app)

#Verificar conexion base de datos
with app.app_context():
    try:
        print("La conexion a la base de datos se establecio correctamente.")
    except Exception as e:
        print("Error al conectar a la base de datos:", str(e))


#actualizar cambios de base de datos
migrate = Migrate()
migrate.init_app(app, conexion)


#Para llamar los modelos y crearlos
from models.usuarios import *


#Para que cree los modelos tablas 
with app.app_context():
    conexion.create_all()





#Llamar los cotrollers
from controllers.inicio_sesion import inicio
from controllers.dashboard.dashboard import dashboard



#Registrar los blueprints 
app.register_blueprint(inicio)
app.register_blueprint(dashboard)
app.register_blueprint(cerrar_sesion)




#Registro del manejador de errores 404
#app.register_error_handler(404, pagina_no_encontrada)