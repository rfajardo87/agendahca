from masonite.middleware import Middleware
from masonite.request import Request


class AuthenticationMiddleware(Middleware):
    """Middleware to check if the user is logged in."""

    def before(self, request: Request, response, is_auth):
        print("ejecutando middle")
        if not request.user():
            return {"session": None, "perfil": None, "perfil_id": None}
        return request

    def after(self, request, response):
        return request
