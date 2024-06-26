#! ../env/bin/python

import click
from flask import Flask, current_app, url_for
from flask.cli import with_appcontext
from webassets.loaders import PythonLoader as PythonAssetsLoader

from appname import assets
from appname.models import db
from appname.controllers.main import main
from mongoengine import connect as mongoengineConnect

from appname.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize mongoEngine
    mongoengineConnect(app.config.get('MONGO_DATABASE_URI'))

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    return app
