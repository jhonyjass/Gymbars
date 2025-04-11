from marshmallow import Schema, fields, validates, ValidationError, pre_load
from datetime import date



class suscripcion_schema(Schema):
    id_cliente = fields.Integer(required=True)
    plan = fields.Integer(required=True)
    estado = fields.Boolean(required=False)
    fecha_suscripcion = fields.Date(required=True)

    @pre_load
    def add_defaults(self, data, **kwargs):
        if "id_cliente" not in data:
            data["id_cliente"] = self.context.get("id_cliente")
        if "fecha_suscripcion" not in data:
            data["fecha_suscripcion"] = date.today().isoformat()
        return data