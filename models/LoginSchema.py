from webargs import fields, validate


LoginSchema = {
    "data": fields.Nested({"email": fields.Str(required=True),
                           "password": fields.Str(required=True, validate=validate.Length(min=6))})

}
