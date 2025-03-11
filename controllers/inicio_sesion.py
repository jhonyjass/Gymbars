from flask import render_template, request, redirect, url_for, flash, session
from config.rutas import inicio
from models.usuarios import *



@inicio.route('/', methods = ['GET','POST'])
def iniciar_sesion():

    if request.method == 'POST':
        try:
            #Captura los datos del formulario
            usuario_ingresado = request.form['usuario']
            contraseña_ingresada = request.form['contraseña']
                
            #Verificar si el usuario existe en la base de datos
            usuario_ingresado = usuarios.query.filter_by(usuario=usuario_ingresado).first()
                
            #Verificar los datos ingresados
            if usuario_ingresado:

                #Verificar si la contraseña es correcta
                if usuario_ingresado.verificar_contraseña(contraseña_ingresada):
                        
                    #Obtener el tipo de usuario
                    tipo_usuario_ingresado = tipo_usuarios.query.get(usuario_ingresado.id_tipo_usuario)

                    #Iniciar sesión
                    session['usuario'] = {
                        'id_usuario': usuario_ingresado.id_usuario,
                        'usuario': usuario_ingresado.usuario,
                        'nombre': usuario_ingresado.nombre,
                        'tipo_usuario': tipo_usuario_ingresado.tipo_usuario
                    }

                    #Ver los datos para asegurar sesion
                    #print(session['usuario'])  
                    return redirect('dashboard') 
                
                # else:
                #     flash('Contraseña incorrecta', 'error')
                #     return redirect(url_for('inicio.iniciar_sesion'))
            else:
                flash('Credenciales incorrectas', 'error')
                return redirect(url_for('inicio.iniciar_sesion'))
            
        except Exception as e:
            print(e)
            flash('al iniciar sesion. Por favor, inténtelo de nuevo.', 'error')
            return redirect(url_for('inicio.iniciar_sesion'))


    return render_template('inicio_sesion.html')