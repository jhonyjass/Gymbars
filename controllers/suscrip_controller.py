from flask import request, render_template, redirect, url_for, flash
from routes.rutas import suscripciones_bp
from services.clientes_service import ClientesService
from services.suscrip_service import SuscripcionesService
from schemas.sucrip_schemas import *



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