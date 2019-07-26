from flask_restful import Resource
from functionality.login import login


class Login(Resource):
    def get(self):
        return login()
