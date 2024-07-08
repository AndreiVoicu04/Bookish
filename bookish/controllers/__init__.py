from bookish.controllers.login import login_routes
from bookish.controllers.library import library_routes
from bookish.controllers.list import list_routes


def register_controllers(app):
    login_routes(app)
    library_routes(app)
    list_routes(app)
