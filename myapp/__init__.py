from flask import Flask

from myapp.models.classa import ClassA
from myapp.models.classb import ClassB


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        a = ClassA()
        b = ClassB()
        return "Hello, World!"

    return app

