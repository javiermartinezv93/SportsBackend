from flask import Flask
from flask_restful import Api

from .resources.admin import Admin

app = Flask(__name__)
api = Api(app)

api.add_resource(Admin, '/admin')