from flask_restful import Resource

from functionality.callback import login_callback
from database import session


class LoginCallback(Resource):
    def get(self):
        response = login_callback()
        session.commit()
        return response
