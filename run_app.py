import os
from app_2 import create_flask_app
from constants.common_constants import FLASK_CONFIG_MODULE
from database import get_session
from restful_apis import create_restful_api
from utils import config_logger

app = create_flask_app('OpenId Connect')
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config.from_object(FLASK_CONFIG_MODULE)

database_url = app.config.get('SQLALCHEMY_DATABASE_URI')
if not database_url:
    raise ValueError('DATABASE-URL-NOT-FOUND')

session = get_session(database_url)

config_logger(app)
create_restful_api(app)


def close_session(resp):
    session.close()  # used to remove actual session
    # session.remove() https://groups.google.com/forum/#!msg/sqlalchemy/twoHzgXcR60/nZqMKkCz9UwJ
    return resp

app.teardown_request(close_session)
app.teardown_appcontext(close_session)


if __name__ == '__main__':
    app.run(debug=False, ssl_context="adhoc")
    # https://stackoverflow.com/questions/14814201/can-i-serve-multiple-clients-using-just-flask-app-run-as-standalone
