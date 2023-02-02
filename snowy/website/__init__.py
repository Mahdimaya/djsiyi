from flask import Flask
import sqlalchemy
from os import path

db = sqlalchemy()

DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '1234567890' 
  app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  from .models import Utilisateurs

  create_database(app)
  
  return app

def create_database(app):
  if not path('website/' +DB_NAME):
    db.create_all(app=app)
    print('Created Database!')
     
