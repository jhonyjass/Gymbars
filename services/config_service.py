from repositories.config_repo import ConfigRepository
from models.usuarios import *


class ConfigService:
    
    @staticmethod
    def tipos_usuarios():
        return ConfigRepository.obtener_tipos_usuario()
    
    @staticmethod
    def lista_usuarios_excluyendo_session(id_usuario_sesion):
        return ConfigRepository.obtener_usuarios_excluyendo_session(id_usuario_sesion)


    @staticmethod
    def agregar_usuario(data):
        # Verificar si el usuario ya existe
        if ConfigRepository.usuario_existe(data['usuario']):
            return 'El nombre de usuario ya existe'

        usuario = usuarios(
            nombre=data['nombre'],
            usuario=data['usuario'],
            contraseña=data['contraseña'],
            id_tipo_usuario=data['tipo_usuario']
        )

        ConfigRepository.agregar_usuario(usuario)

        return True
    
    @staticmethod
    def eliminar_usuario(id_usuario):
        return ConfigRepository.eliminar_usuario(id_usuario)
