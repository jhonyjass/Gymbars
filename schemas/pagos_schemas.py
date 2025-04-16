from marshmallow import Schema, fields, validates, ValidationError, pre_load


class pagos_schema(Schema):
    id_pago = fields.Integer(required=False)
    mensualidad = fields.Integer(required=False)
    fecha_pago = fields.Date(required=True)
    monto = fields.Float(required=True)
    nota = fields.String(required=True)
    tipo_pago = fields.Integer(required=True)