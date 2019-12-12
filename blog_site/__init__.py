from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import random


app = Flask(__name__)

db_info = {
    'host': 'localhost',
    'database': 'blog',
    'user': 'postgres',
    'port': '5432'
}

app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG']= True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres@localhost/blog"
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)

from blog_site import models, routes

app.register_blueprint(routes.main_routes)