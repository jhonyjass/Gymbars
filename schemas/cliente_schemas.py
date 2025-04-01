from marshmallow import Schema, fields, validates, ValidationError, pre_load
from datetime import datetime, date



class telefono_schema(Schema):
    id_cliente = fields.Integer(required=False) 
    telefono = fields.String(required=True)
    tipo_telefono = fields.String(required=True)


class cliente_schema(Schema):
    nombre = fields.String(required=True)
    dpi = fields.Integer(required=True)
    fecha_nacimiento = fields.Date(required=True)
    edad = fields.Integer(required=True)
    sexo = fields.String(required=True)
    grupo_sanguineo = fields.String(required=True)
    correo = fields.Email(required=True)
    fecha_inscripcion = fields.Date(required=True)
    objetivo = fields.Integer(required=True)
    direccion = fields.String(required=True)
    hipertension_arterial = fields.Boolean(required=False)
    diabetes = fields.Boolean(required=False)
    afecciones_alergicas = fields.Boolean(required=False)
    afecciones_respiratorias = fields.Boolean(required=False)
    afecciones_cardiovasculares = fields.Boolean(required=False)
    afecciones_osteoarticulares = fields.Boolean(required=False)
    fuma = fields.Boolean(required=False)
    consume_alcohol = fields.Boolean(required=False)

    # Lista de telefonos
    telefonos = fields.List(fields.Nested(telefono_schema()), required=False)

    @pre_load
    def add_defaults(self, data, **kwargs):
        if "fecha_inscripcion" not in data:
            data["fecha_inscripcion"] = date.today().isoformat()
        return data



class medidas_schema(Schema):
    id_cliente = fields.Integer(required=True)
    fecha_hora = fields.DateTime(required=True)
    cuello = fields.Float(required=True)
    pecho = fields.Float(required=True)
    brazo_derecho = fields.Float(required=True)
    brazo_izquierdo = fields.Float(required=True)
    antebrazo_derecho = fields.Float(required=True)
    antebrazo_izquierdo = fields.Float(required=True)
    cintura = fields.Float(required=True)
    cadera = fields.Float(required=True)
    muslo_derecho = fields.Float(required=True)
    muslo_izquierdo = fields.Float(required=True)
    pantorilla_derecha = fields.Float(required=True)
    pantorilla_izquierda = fields.Float(required=True)
    muñeca_derecha = fields.Float(required=True)
    muñeca_izquierda = fields.Float(required=True)
    tobillo_derecho = fields.Float(required=True)
    tobillo_izquierdo = fields.Float(required=True)
    peso_corporal = fields.Float(required=True)

    @pre_load
    def add_defaults(self, data, **kwargs):
        if "id_cliente" not in data:
            data["id_cliente"] = self.context.get("id_cliente")
        if "fecha_hora" not in data:
            data["fecha_hora"] = datetime.now().isoformat()
        return data