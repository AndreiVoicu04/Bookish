from bookish.controllers.Login_Controller import login_routes
from bookish.controllers.Library_Controller import library_routes
from bookish.controllers.Return_Controller import return_routes


def register_controllers(app):
    login_routes(app)
    library_routes(app)
    return_routes(app)
