from marshmallow import Schema, fields, validates, ValidationError, pre_load


class usuarios_schema(Schema):
    id_usuario = fields.Integer(required=False)
    nombre = fields.String(required=True)
    usuario = fields.String(required=True)
    contraseña = fields.String(required=True)
    tipo_usuario = fields.Integer(required=True)