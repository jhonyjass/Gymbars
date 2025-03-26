from flask import request, render_template, redirect, url_for, flash
from services.clientes_service import ClientesService
from routes.rutas import clientes_bp
from datetime import date,datetime



@clientes_bp.route('/')
def lista_clientes():
    clientes = ClientesService.obtener_clientes()
    return render_template('clientes/clientes.html', clientes = clientes)



@clientes_bp.route('/nuevo_cliente', methods=['GET', 'POST'])
def nuevo_cliente():
    
    objetivos = ClientesService.obtener_objetivos()

    if request.method == 'POST':
        
        try:

            # Cliente
            nombre = request.form['nombre']
            dpi = int(request.form['dpi'])
            fecha_nacimiento = datetime.strptime(request.form['fecha_nacimiento'], '%Y-%m-%d').date()
            edad = int(request.form['edad'])
            sexo = request.form['sexo']
            grupo_sanguineo = request.form['grupo_sanguineo']
            correo = request.form['correo']
            fecha_inscripcion = date.today()
            id_objetivo = int(request.form['objetivo'])

            # Afecciones
            hipertension_arterial = True if request.form.get('hipertension_arterial') == 'on' else False
            diabetes = True if request.form.get('diabetes') == 'on' else False
            afecciones_alergicas = True if request.form.get('afecciones_alergicas') == 'on' else False
            afecciones_respiratorias = True if request.form.get('afecciones_respiratorias') == 'on' else False
            afecciones_cardiovasculares = True if request.form.get('afecciones_cardiovasculares') == 'on' else False
            afecciones_osteoarticulares = True if request.form.get('afecciones_osteoarticulares') == 'on' else False
            fuma = True if request.form.get('fuma') == 'on' else False
            consume_alcohol = True if request.form.get('consume_alcohol') == 'on' else False

            # Crear cliente
            cliente_data = {
                'nombre': nombre,
                'dpi': dpi,
                'fecha_nacimiento': fecha_nacimiento,
                'edad': edad,
                'sexo': sexo,
                'grupo_sanguineo': grupo_sanguineo,
                'correo': correo,
                'fecha_inscripcion': fecha_inscripcion,
                'id_objetivo': id_objetivo
            }
            cliente = ClientesService.agregar_cliente(cliente_data)

            # Crear direccion cliente
            direccion = request.form['direccion']
            direccion_data = {
                'id_cliente': cliente.id_cliente,
                'direccion': direccion
            }
            ClientesService.agregar_direcciones(direccion_data)
            
            # Telefonos cliente
            for key in request.form:
                if key.startswith("telefono_"):
                    index = key.split("_")[-1]
                    numero_tel = request.form.get(f'telefono_{index}')
                    tipo_tel = request.form.get(f'tipo_tel_{index}')
                    # Crear telefonos cliente
                    if numero_tel and tipo_tel:
                        telefono_data = {
                            'id_cliente': cliente.id_cliente,
                            'telefono': numero_tel,
                            'tipo_telefono': tipo_tel
                        }
                        ClientesService.agregar_telefonos(telefono_data)
                    else:
                        print(f"Datos de teléfono incompletos para el teléfono {index}")

            # Crear afecciones
            afeccion_data = {
                'id_cliente': cliente.id_cliente,
                'hipertension_arterial': hipertension_arterial,
                'diabetes': diabetes,
                'afecciones_alergicas': afecciones_alergicas,
                'afecciones_respiratorias': afecciones_respiratorias,
                'afecciones_cardiovasculares': afecciones_cardiovasculares,
                'afecciones_osteoarticulares': afecciones_osteoarticulares,
                'fuma': fuma,
                'consume_alcohol': consume_alcohol
            }
            ClientesService.agregar_afecciones(afeccion_data)
            
            flash('Cliente agregado correctamente.', 'success')
            return redirect(url_for('clientes_bp.lista_cliente'))
        
        except Exception as e:
            flash('Error al agregar cliente', 'danger')
            print(str(e))
            return redirect(url_for('clientes_bp.nuevo_cliente'))

    return render_template('clientes/nuevo_cliente.html', objetivos=objetivos)

