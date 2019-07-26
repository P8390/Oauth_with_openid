from flask import request, redirect
from flask import current_app as app
from oauthlib.oauth2 import WebApplicationClient

from utils import get_google_provider_cfg


def get_auth_client():
    client = WebApplicationClient(app.config.get('GOOGLE_CLIENT_ID'))
    return client


def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    client = get_auth_client()
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)
