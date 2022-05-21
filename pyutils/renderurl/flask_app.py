from random import shuffle
from typing import List

from flask import Flask, render_template
from pyutils.renderurl.secret import app_pass
from flask import request
app = Flask(
    __name__,
)
from flask import abort
from splinter import Browser


@app.route("/", methods=["GET"])
def fetch() -> str:
    """
    Endpoint to fetch ui.

    Returns:
        Processed html string
    """
    if app_pass != request.args.get('app_pass', ''):
        abort(404)
        return ""

    with Browser("chrome", headless=True, capabilities={'acceptSslCerts': True}, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0") as browser:
        browser.visit(request.args["url"])

        return browser.html

    


if __name__ == "__main__":
    port = 8883
    app.run(host="127.0.0.1", port=port, debug=False)  # noqa:S104,S201
