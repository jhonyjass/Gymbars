from flask import flash, session, redirect, url_for
from repositories.usuario_repo import UsuarioRepository
import bcrypt


class SesionService:

    @staticmethod
    def validar_usuario(usuario_ingresado, contraseña_ingresada):
        try:
            usuario_encontrado = UsuarioRepository.obtener_usuario_por_usuario(usuario_ingresado)
            
            if usuario_encontrado and usuario_encontrado.verificar_contraseña(contraseña_ingresada):
                tipo_usuario = UsuarioRepository.obtener_tipo_usuario_por_id(usuario_encontrado.id_tipo_usuario)
                
                # Crear sesion
                session['usuario'] = {
                    'id_usuario': usuario_encontrado.id_usuario,
                    'usuario': usuario_encontrado.usuario,
                    'nombre': usuario_encontrado.nombre,
                    'tipo_usuario': tipo_usuario.tipo_usuario
                }
                return True  
            else:
                return False  

        except Exception as e:
            return str(e) 


    @staticmethod
    def editar_usuario(nuevo_nombre=None, nuevo_usuario=None, nueva_contraseña=None):
        try:
            usuario_actual = UsuarioRepository.usuario_actual()
            usuario_actualizar = UsuarioRepository.obtener_usuario_por_id(usuario_actual['id_usuario'])

            if not usuario_actual or not usuario_actualizar:
                return "Usuario no encontrado"

            # Verificar si no se realizaron cambios
            if (
                (not nuevo_nombre or nuevo_nombre == usuario_actualizar.nombre) and
                (not nuevo_usuario or nuevo_usuario == usuario_actualizar.usuario) and
                (not nueva_contraseña)
            ):
                return "No se realizaron cambios"

            # Verificar si el nuevo usuario ya existe
            if nuevo_usuario and nuevo_usuario != usuario_actualizar.usuario:
                usuario_existente = UsuarioRepository.obtener_usuario_por_usuario(nuevo_usuario)
                if usuario_existente:
                    return "El usuario ya existe"

            # Actualizar los campos
            if nuevo_nombre:
                usuario_actualizar.nombre = nuevo_nombre
            if nuevo_usuario:
                usuario_actualizar.usuario = nuevo_usuario
            if nueva_contraseña:
                hashed_nueva_contraseña = bcrypt.hashpw(nueva_contraseña.encode('utf-8'), bcrypt.gensalt())
                usuario_actualizar.contraseña = hashed_nueva_contraseña.decode('utf-8')

            # Guardar cambios 
            UsuarioRepository.guardar_cambios_perfil(usuario_actualizar)
            session['usuario']['nombre'] = nuevo_nombre if nuevo_nombre else usuario_actualizar.nombre
            session['usuario']['usuario'] = nuevo_usuario if nuevo_usuario else usuario_actualizar.usuario

            return "Perfil actualizado correctamente"

        except Exception as e:
            return f"Error al actualizar perfil: {str(e)}"

