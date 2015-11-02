from app.Models.hub import Hub
from app.DataBase.database import db_session

from flask.ext.restful import reqparse, abort, Resource, fields, marshal_with


hub_fields = {
    'id': fields.Integer,
    'name': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


class HubResource(Resource):
    @marshal_with(hub_fields)
    def get(self, id):
        hub = db_session.query(Hub).filter(Hub.id == id).first()
        if not hub:
            abort(404, message="Hub doesn't exist".format(id))
        return hub

    def put(self):
        parsed_args = parser.parse_args()
        hub = Hub(name=parsed_args['name'])
        db_session.add(hub)
        db_session.commit()
        return todo, 201


    def delete(self, todo_id):


        return '', 204


class HubListResource(Resource):
    @marshal_with(hub_fields)
    def get(self):
        hubs = db_session.query(Hub).all()
        return hubs, 201

    def post(self):
        parsed_args = parser.parse_args()
        hub = Hub(name=parsed_args['name'])
        db_session.add(hub)
        db_session.commit()
        return hub.as_dict(), 201
