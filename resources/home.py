from flask_restful import Resource

from functionality.home import index


class Home(Resource):
    def get(self):
        return index()
