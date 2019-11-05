from flask import Flask

from myapp.models.classa import ClassA


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        a = ClassA()
        b = a.get_b()
        return "Hello, world!"

    return app

