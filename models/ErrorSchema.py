from webargs import fields, validate
from marshmallow import Schema


class ErrorSchema(Schema):
    message = fields.Str(required=False)
