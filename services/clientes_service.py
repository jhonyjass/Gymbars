from repositories.clientes_repo import ClientesRepository
from models.clientes import *


class ClientesService:
    
    @staticmethod
    def obtener_clientes():
        return ClientesRepository.listado_clientes()
    
    @staticmethod
    def obtener_cliente_id(id_cliente):
        return ClientesRepository.obtener_cliente_por_id(id_cliente)

    @staticmethod
    def obtener_objetivos():
        return ClientesRepository.objetivos_para_cliente()


    @staticmethod
    def agregar_cliente(cliente_data):
        cliente = clientes(
            nombre = cliente_data['nombre'],
            dpi = cliente_data['dpi'],
            fecha_nacimiento = cliente_data['fecha_nacimiento'],
            edad = cliente_data['edad'],
            sexo = cliente_data['sexo'],
            grupo_sanguineo = cliente_data['grupo_sanguineo'],
            correo = cliente_data['correo'],
            id_objetivo = cliente_data['id_objetivo'],
            fecha_inscripcion = cliente_data['fecha_inscripcion'],
        )
        ClientesRepository.agregar_cliente(cliente)

        return cliente


    @staticmethod
    def agregar_telefonos(telefono_data):
        telefono = telefonos(
            id_cliente = telefono_data['id_cliente'],
            telefono = telefono_data['telefono'],
            tipo_telefono = telefono_data['tipo_telefono']
        )
        ClientesRepository.agregar_telefonos_cliente(telefono)

        return True

    @staticmethod
    def agregar_afecciones(afeccion_data):
        afeccion = afecciones(
            id_cliente = afeccion_data['id_cliente'],
            hipertension_arterial = afeccion_data['hipertension_arterial'],
            diabetes = afeccion_data['diabetes'],
            afecciones_alergicas = afeccion_data['afecciones_alergicas'],
            afecciones_respiratorias = afeccion_data['afecciones_respiratorias'],
            afecciones_cardiovasculares = afeccion_data['afecciones_cardiovasculares'],
            afecciones_osteoarticulares = afeccion_data['afecciones_osteoarticulares'],
            fuma = afeccion_data['fuma'],
            consume_alcohol = afeccion_data['consume_alcohol']
        )
        ClientesRepository.agregar_afecciones_cliente(afeccion)

        return True

    @staticmethod
    def agregar_direcciones(direccion_data):
        direccion = direcciones(
            id_cliente = direccion_data['id_cliente'],
            direccion = direccion_data['direccion']
        )
        ClientesRepository.agregar_direcciones_cliente(direccion)

        return True
    

    @staticmethod
    def agregar_medidas_cliente(medidas_data):
        medidas_cliente = medidas(
            id_cliente = medidas_data['id_cliente'],
            fecha_hora=medidas_data['fecha_hora'],
            cuello = medidas_data['cuello'],
            pecho = medidas_data['pecho'],
            brazo_derecho = medidas_data['brazo_derecho'],
            brazo_izquierdo = medidas_data['brazo_izquierdo'],
            antebrazo_derecho = medidas_data['antebrazo_derecho'],
            antebrazo_izquierdo = medidas_data['antebrazo_izquierdo'],
            cintura = medidas_data['cintura'],
            cadera = medidas_data['cadera'],
            muslo_derecho = medidas_data['muslo_derecho'],
            muslo_izquierdo = medidas_data['muslo_izquierdo'],
            pantorilla_derecha = medidas_data['pantorilla_derecha'],
            pantorilla_izquierda = medidas_data['pantorilla_izquierda'],
            muñeca_derecha = medidas_data['muñeca_derecha'],
            muñeca_izquierda = medidas_data['muñeca_izquierda'],
            tobillo_derecho = medidas_data['tobillo_derecho'],
            tobillo_izquierdo = medidas_data['tobillo_izquierdo'],
            peso_corporal = medidas_data['peso_corporal']
        )

        ClientesRepository.agregar_medidas_cliente(medidas_cliente)

        return True
    


    @staticmethod
    def editar_telefono(telefono_data):
        telefono = ClientesRepository.obtener_telefono_por_id(telefono_data['id_telefono'])

        if telefono:
            telefono.telefono = telefono_data['telefono']
            telefono.tipo_telefono = telefono_data['tipo_telefono']
            ClientesRepository.actualizar_telefono(telefono)


    @staticmethod
    def eliminar_telefono(id_telefono):
        telefono = ClientesRepository.obtener_telefono_por_id(id_telefono)

        if telefono:
            ClientesRepository.eliminar_telefono(telefono)