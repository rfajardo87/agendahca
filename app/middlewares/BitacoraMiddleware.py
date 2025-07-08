# Copyright (C) 2023 Rubén de Jesús Fajardo Jaime
#
# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU tal como está
# publicada por la Fundación para el Software Libre, ya sea la versión 3
# de la Licencia, o (a tu elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil, pero
# SIN GARANTÍA ALGUNA; sin siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Véase la
# Licencia Pública General de GNU para más detalles.
#
# Debes haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no, consulta <https://www.gnu.org/licenses/>.

from datetime import datetime

from masonite.middleware import Middleware

from app.models.Log import Log
from app.models.Session import Session

from ..bitacora.Bitacora import Bitacora


class BitacoraMiddleware(Middleware):
    """Bitacora middleware"""

    def before(self, request, response):
        ruta = request.get_path()
        session = {"curp": "sistema"}
        if ruta != "/session":
            session_code = request.header("session")
            if ruta == "/template/horario":
                session_code = request.input("session")
            session = Session.where({"session": session_code}).first().serialize()

        datos = f"{request.all()}"
        metodo = request.get_request_method()

        kwargs = {
            "curp": session["curp"],
            "ruta": ruta,
            "metodo": metodo,
            "datos": datos,
            "fecha": datetime.now(),
            "level": "info",
        }
        Log.create(kwargs)
        return request

    def after(self, request, response):
        return request
