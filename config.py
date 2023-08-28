import os


# Mengambil url path lokasi dari flask app (current directory)
basedir = os.path.abspath(os.path.dirname(__file__))

# Menentukan lokasi di mana database akan di simpan
DB_PATH = 'sqlite:///' + os.path.join(basedir, 'app.db')

# 
class Config: 
    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False