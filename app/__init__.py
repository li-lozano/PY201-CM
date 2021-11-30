#
import os
from flask import Flask

#
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )
    # database
    from . import db
    db.init_app(app)

    # blueprints
    from . import contact
    app.register_blueprint(contact.bp)

    return app

