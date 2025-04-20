from flask import request, render_template, redirect, url_for, flash, session
from routes.rutas import config_bp
from services.config_service import ConfigService
from schemas.config_schemas import *
from utils.decoradores import *



@config_bp.route('/', methods=['GET', 'POST'])
@administrador_requerido
def configuraciones():
    
    tipos_usuarios = ConfigService.tipos_usuarios()
    id_usuario_sesion = session['usuario']['id_usuario']
    usuarios = ConfigService.lista_usuarios_excluyendo_session(id_usuario_sesion)

    return render_template('configuracion/configuracion.html',
                           tipos_usuarios=tipos_usuarios,
                           usuarios=usuarios)



@config_bp.route('/nuevo_usuario', methods=['GET', 'POST'])
@administrador_requerido
def nuevo_usuario():
    if request.method == 'POST':
        try:
            usuario_data = request.form.to_dict()
            usuario_esquema = usuarios_schema()
            usuario_validado = usuario_esquema.load(usuario_data)
            resultado = ConfigService.agregar_usuario(usuario_validado)

            if resultado == True:
                flash('Usuario guardado correctamente', 'success')
                return redirect(url_for('config_bp.configuraciones'))
            else:
                flash(resultado, 'error')
                return redirect(url_for('config_bp.configuraciones'))
        except Exception as e:
            flash('Error al guardar usuario', 'error')
            print(e)
            return redirect(url_for('config_bp.configuraciones'))

    return redirect(url_for('config_bp.configuraciones'))



@config_bp.route('/eliminar_usuario/<int:id_usuario>', methods=['GET','POST'])
@administrador_requerido
def eliminar_usuario(id_usuario):
    resultado = ConfigService.eliminar_usuario(id_usuario)

    if resultado == True:
        flash('Usuario eliminado correctamente', 'success')
    else:
        flash(resultado, 'error')

    return redirect(url_for('config_bp.configuraciones'))