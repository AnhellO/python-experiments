from marshmallow import fields

from app.ext import ma


class FilmSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    length = fields.Integer()
    year = fields.Integer()
    director = fields.String()
    actors = fields.Nested('ActorSchema', many=True)


class ActorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()