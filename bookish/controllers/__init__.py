from bookish.controllers.login_controller import login_routes
from bookish.controllers.library_controller import library_routes
from bookish.controllers.return_controller import return_routes


def register_controllers(app):
    login_routes(app)
    library_routes(app)
    return_routes(app)
