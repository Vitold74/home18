from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace("genres")
@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        genre = genre_service.get_all()
        return GenreSchema(many=True).dump(genre), 200

@genres_ns.route("/<int:bid")
class GenresView(Resource):
    def get(self, bid):
        genre = genre_service.get_one(bid)
        return GenreSchema().dump(genre), 200