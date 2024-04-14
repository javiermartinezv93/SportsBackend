from flask_restful import Resource

class Admin(Resource):

    @classmethod
    def get(cls):
        return {"message": "Hi "}, 200

