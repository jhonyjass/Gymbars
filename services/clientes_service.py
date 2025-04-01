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
    def obtener_info_cliente_id(id_cliente):
        return ClientesRepository.obtener_info_cliente(id_cliente)

    @staticmethod
    def obtener_objetivos():
        return ClientesRepository.objetivos_para_cliente()


    @staticmethod
    def agregar_cliente(cliente_data):

        # Crear cliente
        cliente = clientes(
            nombre = cliente_data['nombre'],
            dpi = cliente_data['dpi'],
            fecha_nacimiento = cliente_data['fecha_nacimiento'],
            edad = cliente_data['edad'],
            sexo = cliente_data['sexo'],
            grupo_sanguineo = cliente_data['grupo_sanguineo'],
            correo = cliente_data['correo'],
            id_objetivo = cliente_data['objetivo'],
            fecha_inscripcion = cliente_data['fecha_inscripcion'],
        )

        # Agregar cliente
        ClientesRepository.agregar_cliente(cliente)

        # Obtener el id del cliente 
        cliente_id = cliente.id_cliente

        # Agregar direccion
        direccion = direcciones(
            id_cliente = cliente_id,
            direccion = cliente_data['direccion']
        )
        ClientesRepository.agregar_direcciones_cliente(direccion)

        # Agregar afecciones
        afeccion = afecciones(
            id_cliente = cliente_id,
            hipertension_arterial = cliente_data.get('hipertension_arterial', False),
            diabetes = cliente_data.get('diabetes', False),
            afecciones_alergicas = cliente_data.get('afecciones_alergicas', False),
            afecciones_respiratorias = cliente_data.get('afecciones_respiratorias', False),
            afecciones_cardiovasculares = cliente_data.get('afecciones_cardiovasculares', False),
            afecciones_osteoarticulares = cliente_data.get('afecciones_osteoarticulares', False),
            fuma = cliente_data.get('fuma', False),
            consume_alcohol = cliente_data.get('consume_alcohol', False)
        )
        ClientesRepository.agregar_afecciones_cliente(afeccion)

        # Agregar telefonos
        if 'telefonos' in cliente_data:
            for telefono in cliente_data['telefonos']:
                telefono_data = {
                    'id_cliente': cliente_id,
                    'telefono': telefono['telefono'],
                    'tipo_telefono': telefono['tipo_telefono']
                }
                ClientesService.agregar_telefonos(telefono_data)

        return cliente



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
    def agregar_telefonos(telefono_data):
        telefono = telefonos(
            id_cliente = telefono_data['id_cliente'],
            telefono = telefono_data['telefono'],
            tipo_telefono = telefono_data['tipo_telefono']
        )
        ClientesRepository.agregar_telefonos_cliente(telefono)

        return True


    @staticmethod
    def editar_telefono(telefono_data):
        telefono = ClientesRepository.obtener_telefono_por_id(telefono_data['id_telefono'])

        telefono_antes = str(telefono.telefono).strip()
        tipo_telefono_antes = str(telefono.tipo_telefono).strip()
        
        # Actualiza solo si hay cambios
        telefono.telefono = str(telefono_data.get('telefono', telefono.telefono)).strip()
        telefono.tipo_telefono = str(telefono_data.get('tipo_telefono', telefono.tipo_telefono)).strip()
        
        # Verifica si los valores han cambiado
        if telefono_antes == telefono.telefono and tipo_telefono_antes == telefono.tipo_telefono:
            return False
        
        ClientesRepository.actualizar_telefono(telefono)
        
        return True


    @staticmethod
    def eliminar_telefono(id_telefono):
        telefono = ClientesRepository.obtener_telefono_por_id(id_telefono)

        if telefono:
            ClientesRepository.eliminar_telefono(telefono)
        
        return True