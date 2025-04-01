from flask import request, render_template, redirect, url_for, flash
from services.clientes_service import ClientesService
from routes.rutas import clientes_bp
from schemas.cliente_schemas import *


@clientes_bp.route('/')
def lista_clientes():
    clientes = ClientesService.obtener_clientes()
    return render_template('clientes/clientes.html', clientes = clientes)



@clientes_bp.route('/nuevo_cliente', methods=['GET', 'POST'])
def nuevo_cliente():
    
    objetivos = ClientesService.obtener_objetivos()

    if request.method == 'POST':
        try:
            # Diccionario datos
            cliente_data = request.form.to_dict()

            telefonos = []
            phone_index = 1

            while f"telefono_{phone_index}" in cliente_data:
                telefono_info = {
                    "telefono": cliente_data.pop(f"telefono_{phone_index}"),
                    "tipo_telefono": cliente_data.pop(f"tipo_tel_{phone_index}")
                }
                telefonos.append(telefono_info)
                phone_index += 1

            # Agregar la lista de tel a dic
            cliente_data["telefonos"] = telefonos

            cliente_esquema = cliente_schema()
            cliente_data = cliente_esquema.load(cliente_data)
            ClientesService.agregar_cliente(cliente_data)

            flash('Cliente agregado correctamente.', 'success')
            return redirect(url_for('clientes_bp.lista_clientes'))
          
        except Exception as e:
            flash('Error al agregar cliente', 'error')
            print(str(e))
            return redirect(url_for('clientes_bp.nuevo_cliente'))

    return render_template('clientes/nuevo_cliente.html', objetivos=objetivos)



@clientes_bp.route('/informacion_cliente/<int:id_cliente>', methods = ['GET','POST'])
def info_cliente(id_cliente):
    
    cliente = ClientesService.obtener_info_cliente_id(id_cliente)
    
    return render_template('clientes/info_cliente.html', cliente = cliente)



@clientes_bp.route('/nuevas_medidas_cliente/<int:id_cliente>', methods = ['GET', 'POST'])
def nuevas_medidas_cliente(id_cliente):

    cliente = ClientesService.obtener_info_cliente_id(id_cliente)

    if request.method == 'POST':
        try:
            
            medidas_data = request.form.to_dict()
            medidas_esquema = medidas_schema()
            medidas_esquema.context = {"id_cliente": id_cliente}
            medidas_validadas = medidas_esquema.load(medidas_data)
            ClientesService.agregar_medidas_cliente(medidas_validadas)
            
            flash('Medidas guardadas correctamente', 'success')
            return redirect(url_for('clientes_bp.info_cliente', id_cliente = id_cliente))

        except Exception as e:
            flash('Error al agregar medidas de cliente', 'error')
            print(str(e))
            return redirect(url_for('clientes_bp.nuevas_medidas_cliente', id_cliente = id_cliente))

    return render_template('clientes/nuevas_medidas_cliente.html', cliente = cliente)



@clientes_bp.route('/todas_las_medidas_cliente/<int:id_cliente>', methods = ['GET', 'POST'])
def todas_medidas_cliente(id_cliente):

    cliente = ClientesService.obtener_info_cliente_id(id_cliente)

    return render_template('clientes/todas_medidas_cliente.html', cliente = cliente)



@clientes_bp.route('/nuevo_telefono_cliente/<int:id_cliente>', methods = ['GET', 'POST'])
def nuevo_tel_cliente(id_cliente):

    if request.method == 'POST':
        try:
            
            telefono_data = request.form.to_dict()
            telefono_data["id_cliente"] = id_cliente
            telefono_esquema = telefono_schema()
            telefono_validado = telefono_esquema.load(telefono_data)
            ClientesService.agregar_telefonos(telefono_validado)

            flash('Telefono agregado correctamente.', 'success')
            return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))

        except Exception as e:
            flash('Error al agregar telefono de cliente', 'error')
            print(str(e))
            return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))

    return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))



@clientes_bp.route('/editar_telefono_cliente/<int:id_telefono>', methods=['POST'])
def editar_tel_cliente(id_telefono):
    try:
        
        telefono_data = request.form.to_dict()
        telefono_esquema = telefono_schema()
        telefono_validado = telefono_esquema.load(telefono_data)
        telefono_validado["id_telefono"] = id_telefono
       
        if not ClientesService.editar_telefono(telefono_validado):
            flash("No se realizaron cambios.", 'error')
        else:
            flash('Teléfono actualizado correctamente.', 'success')

        return redirect(request.referrer)

    except Exception as e:
        flash('Error al actualizar teléfono.', 'error')
        print(str(e))

    return redirect(request.referrer)



@clientes_bp.route('/eliminar_telefono_cliente/<int:id_telefono>', methods=['GET','POST'])
def eliminar_tel_cliente(id_telefono):
    try:
        ClientesService.eliminar_telefono(id_telefono)
        flash('Teléfono eliminado correctamente.', 'success')
        return redirect(request.referrer) 
    except Exception as e:
        flash('Error al eliminar teléfono.', 'error')
        print(str(e))

    return redirect(request.referrer)