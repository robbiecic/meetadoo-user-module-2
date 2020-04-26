from webargs import fields, validate
from marshmallow import Schema


class LoginChildSchema(Schema):
    email = fields.Email()
    password = fields.String()


class LoginSchema(Schema):
    data = fields.Nested(LoginChildSchema)


class LoginResponseSchema(Schema):
    firstname = fields.Str(required=True)
    surname = fields.Str(required=True)
    email = fields.Str(required=True)
