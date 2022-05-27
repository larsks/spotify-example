"""This code implements the authorization code flow [1].

[1]: https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
"""

import flask
import os
import requests

from urllib.parse import urlencode

client_id = os.environ["SPOTIFY_CLIENT_ID"]
client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
redirect_uri = "http://localhost:5000/callback"

app = flask.Flask("spotify-authorization-server")


@app.route("/")
def index():
    return f'<a href="{flask.url_for("login")}">Login</a>'


@app.route("/login")
def login():
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "state": "mystate",
    }
    qs = urlencode(params)
    return flask.redirect(f"https://accounts.spotify.com/authorize?{qs}")


@app.route("/callback")
def callback():
    code = flask.request.args["code"]
    res = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
        },
        auth=(client_id, client_secret),
        allow_redirects=False,
    )

    res.raise_for_status()
    return res.json()
