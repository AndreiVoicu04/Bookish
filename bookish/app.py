import os
from flask import Flask
from bookish.models import db, migrate
from bookish.controllers import register_controllers
from bookish.error_handler import handle_http_exception
from werkzeug.exceptions import HTTPException

def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_error_handler(HTTPException, handle_http_exception)
    db.init_app(app)
    migrate.init_app(app, db)

    register_controllers(app)

    if __name__ == "__main__":
        app.run()

    return app
