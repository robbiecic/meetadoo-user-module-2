from webargs import fields, validate
from marshmallow import Schema


LoginSchema = {
    "data": fields.Nested({"email": fields.Str(required=True),
                           "password": fields.Str(required=True, validate=validate.Length(min=6))})

}


class LoginResponseSchema(Schema):
    firstname = fields.Str(required=True)
    surname = fields.Str(required=True)
    email = fields.Str(required=True)
