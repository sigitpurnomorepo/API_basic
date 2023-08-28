from flask import Flask
from app.user import userbp

from config import Config

def create_app(config_class = Config):
    app = Flask(__name__)
    # existing code omitted
    # Memanggil konfigurasi untuk digunakan oleh flask
    app.config.from_object(config_class)

    
    app.register_blueprint(userbp)
    return app



