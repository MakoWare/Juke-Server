from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


from app.DataBase.database import init_db
init_db()
from app.routes import *



# from serveryourapplication.database import db_session

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()



