import os

from flask import Flask
from . import auth


def start_db(app):
    try:
        from . import db
        db.init_app(app)
    except Exception as Error:
        raise ValueError(Error)


def start_auth(app):
    from . import auth
    app.register_blueprint(auth.bp)


def start_blog(app):
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


def create_instance_folder(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def start_config(app, test_config):
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.db'),
    )
    start_config(app, test_config)
    create_instance_folder(app)

    start_db(app)
    start_auth(app)
    start_blog(app)

    return app

