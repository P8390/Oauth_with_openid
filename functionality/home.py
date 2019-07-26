from flask import render_template, make_response


def index():
    return make_response(render_template('index.html'))
