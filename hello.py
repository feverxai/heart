# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:18:49 2020

@author: TRUE
"""

import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)