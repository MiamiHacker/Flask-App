from flask import Flask

'''
pip install flask 
pip install flask-login 
pip install flask-sqlalchemy
python3 main.py 
'''


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WhatEverYouWant'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app