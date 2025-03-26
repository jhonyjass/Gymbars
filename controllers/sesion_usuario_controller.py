from flask import render_template, redirect, url_for, flash, request, session
from services.sesion_service import SesionService
from routes.rutas import sesion_usuario_bp


@sesion_usuario_bp.route('/', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        try:
            usuario_ingresado = request.form['usuario']
            contraseña_ingresada = request.form['contraseña']

            resultado = SesionService.validar_usuario(usuario_ingresado, contraseña_ingresada)
            
            if resultado is True:
                return redirect(url_for('dashboard_bp.dashboard'))
            else:
                flash('Credenciales incorrectas', 'error')
                return redirect(url_for('sesion_usuario_bp.iniciar_sesion'))

        except Exception as e:
            flash('Error al iniciar sesión', 'error')
            print(str(e))
            return redirect(url_for('sesion_usuario_bp.iniciar_sesion'))

    return render_template('inicio_sesion.html')



@sesion_usuario_bp.route('/perfil', methods = ['GET', 'POST'])
def editar_perfil():
    if request.method == 'POST':
        try:
            nuevo_nombre = request.form['nombre']
            nuevo_usuario = request.form['usuario']
            nueva_contraseña = request.form['contraseña']

            resultado = SesionService.editar_usuario(nuevo_nombre, nuevo_usuario, nueva_contraseña)

            if resultado == "Perfil actualizado correctamente":
                flash(resultado, 'success')
            else:
                flash(resultado, 'error') 

            return redirect(url_for('sesion_usuario_bp.editar_perfil'))

        except Exception as e:
            flash('Error al actualizar perfil', 'error')
            print(str(e))
            return redirect(url_for('sesion_usuario_bp.editar_perfil'))
    
    return render_template('perfil/perfil.html') 



@sesion_usuario_bp.route('/cerrar_session', methods = ['GET'])
def cerrar_session():
    session.pop('usuario', None)
    return redirect(url_for('sesion_usuario_bp.iniciar_sesion'))

