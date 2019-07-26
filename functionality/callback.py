import requests
import json
from flask import current_app as app, request, redirect, url_for
from functionality.login import get_auth_client
from models.user import User
from utils import get_google_provider_cfg


def login_callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens
    client = get_auth_client()
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(app.config.get('GOOGLE_CLIENT_ID'), app.config.get('GOOGLE_CLIENT_SECRET')),
    )
    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    user_info_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(user_info_endpoint)
    user_info_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if user_info_response.json().get("email_verified"):
        unique_id = user_info_response.json()["sub"]
        users_email = user_info_response.json()["email"]
        picture = user_info_response.json()["picture"]
        users_name = user_info_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    user_obj = User.get_user_info(unique_id)
    # dump data into users table
    # print('user object is = {}'.format(user_obj.__dict__))
    if not user_obj:
        params = dict(unique_id=unique_id, name=users_name, email=users_email, profile_pic=picture)
        _ = User.create_new_user(**params)

    # print(app.url_map)
    return redirect(url_for("home_page"))
