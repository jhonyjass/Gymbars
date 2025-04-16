from flask import request, render_template, redirect, url_for, flash
from routes.rutas import suscripciones_bp
from services.clientes_service import ClientesService
from services.suscrip_service import SuscripcionesService
from services.pagos_service import PagosService
from services.clientes_service import ClientesService
from schemas.sucrip_schemas import *
from schemas.pagos_schemas import *



@suscripciones_bp.route('/', methods = ['GET','POST'])
def lista_suscripciones():

    suscripciones_activas = SuscripcionesService.obtener_sus_activas()
    suscripciones_inactivas = SuscripcionesService.obtener_sus_inactivas()

    return render_template('suscripciones/suscripciones.html',
                           suscripciones_activas = suscripciones_activas,
                           suscripciones_inactivas = suscripciones_inactivas)


@suscripciones_bp.route('/nueva_suscripcion/<int:id_cliente>', methods = ['GET','POST'])
def agregar_suscripcion(id_cliente):

    cliente = ClientesService.obtener_cliente_id(id_cliente)
    planes = SuscripcionesService.obtener_planes()

    if SuscripcionesService.cliente_tiene_suscripcion(id_cliente):
        flash('Este cliente tiene una suscripción activa.', 'error')
        return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))

    if request.method == 'POST':
        try:
            datos_formulario = request.form.to_dict()
            schema = suscripcion_schema(context={"id_cliente": id_cliente})
            datos_validados = schema.load(datos_formulario)
         
            resultado = SuscripcionesService.crear_suscripcion(datos_validados)

            if resultado is not True:
                flash(resultado, 'error')
                return redirect(url_for('suscripciones_bp.agregar_suscripcion', id_cliente=id_cliente))

            flash('Suscripción creada correctamente.', 'success')
            return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))

        except Exception as e:
            flash('Error al Agregar suscripcion', 'error')
            print(str(e))
            return redirect(url_for('suscripciones_bp.agregar_suscripcion', id_cliente=id_cliente))


    return render_template('suscripciones/nueva_suscripcion.html', 
                           cliente = cliente,
                           planes = planes)




@suscripciones_bp.route('/editar_suscripcion/<int:id_cliente>', methods = ['GET','POST'])
def editar_suscripcion(id_cliente):

    cliente = ClientesService.obtener_cliente_id(id_cliente)
    suscrip_cliente = SuscripcionesService.obtener_suscripcion_cliente(id_cliente)
    planes = SuscripcionesService.obtener_planes()

    if request.method == 'POST':
        try:
            datos = request.form.to_dict()
            datos['id_cliente'] = id_cliente
            data_validada = suscripcion_schema().load(datos)

            resultado = SuscripcionesService.actualizar_suscripcion(data_validada)
            if resultado == True:
                flash('Suscripción actualizada correctamente', 'success')
                return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))
            else:
                flash('Ocurrió un error al actualizar', 'danger')
                return redirect(url_for('clientes_bp.info_cliente', id_cliente=id_cliente))
                
        except Exception as e:
            flash('Error al actualizar suscripcion', 'error')
            print(str(e))
            return redirect(url_for('suscripciones_bp.editar_suscripcion', id_cliente=id_cliente))


    return render_template('suscripciones/actualizar_suscripcion.html', 
                           cliente = cliente,
                           suscrip_cliente = suscrip_cliente,
                           planes = planes)



@suscripciones_bp.route('/suscripcion_estado_cuenta/<int:id_cliente>', methods = ['GET','POST'])
def estado_cuenta_cliente(id_cliente):

    cliente = ClientesService.obtener_cliente_id(id_cliente)
    mensualidades_año = SuscripcionesService.obtener_mensualidades_año_cliente(id_cliente)
    mensualidades_pendientes = SuscripcionesService.obtener_mensualidades_pediente_pago_cliente(id_cliente)
    pagos_cliente_año = PagosService.obtener_pagos_cliente_año(id_cliente) 
    tipo_pagos = PagosService.obtener_tipos_pagos()

    return render_template('suscripciones/estados_de_cuenta.html',
                           cliente = cliente,
                           mensualidades_año = mensualidades_año,
                           mensualidades_pendientes = mensualidades_pendientes,
                           pagos_cliente_año = pagos_cliente_año,
                           tipo_pagos = tipo_pagos)



@suscripciones_bp.route('/agregar_pago', methods=['GET','POST'])
def agregar_pago():
    if request.method == 'POST':
        try:
            datos = request.form.to_dict()
            data_validada = pagos_schema().load(datos)
            resultado = PagosService.guardar_pago(data_validada)

            if resultado == True:
                flash('Pago registrado correctamente', 'success')
                return redirect(request.referrer)
            else:
                flash(resultado, 'error')
                return redirect(request.referrer)
            
        except Exception as e:
            flash('Ocurrió un error al registrar el pago', 'danger')
            print(str(e))
            return redirect(request.referrer)

    return redirect(request.referrer)



@suscripciones_bp.route('/editar_pago/<int:id_pago>', methods=['POST'])
def editar_pago(id_pago):
    if request.method == 'POST':
        try:
            datos = request.form.to_dict()
            data_validada = pagos_schema().load(datos)
            resultado = PagosService.actualizar_pago(id_pago, data_validada)

            if resultado == True:
                flash('Pago actualizado correctamente', 'success')
                return redirect(request.referrer)
            else:
                flash(str(resultado), 'error')
                return redirect(request.referrer)
        except Exception as e:
            flash('Error inesperado al actualizar el pago', 'danger')
            print(str(e))
            return redirect(request.referrer)

    return redirect(request.referrer)


