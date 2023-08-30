from flask import Flask
from app.user import userbp


def create_app():
    app = Flask(__name__)
    # existing code omitted
    # Memanggil konfigurasi untuk digunakan oleh flask

    app.register_blueprint(userbp)
    return app



