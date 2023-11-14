import datetime
import os

from flask_cors import cross_origin

from flask import Blueprint
from flask import request, redirect, send_file, Response
from flask import render_template
from flask.json import jsonify

"""
- Main screen
"""


class SimulatorBP:

    def __init__(self):
        print("Init Simulator.......")
        self.simulator_bp = Blueprint(
            "simulator_bp",
            __name__,
            template_folder="templates",
            static_folder="static",
            static_url_path='/%s' % __name__,
        )

        @self.simulator_bp.route("/", methods=["GET"])
        def home():
            return render_template("simulator.jinja2")

        # Other algorithms