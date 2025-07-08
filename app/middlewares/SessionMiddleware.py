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

from app.models.Session import Session


class SessionMiddleware(Middleware):
    """Sessiom Middleware"""

    def before(self, request, response):

        ruta = request.get_path()

        if ruta in ["/session"]:
            return request

        session_code = request.header("session")

        if ruta == "/template/horario":
            session_code = request.input("session")

        session_relacion = Session.where({"session": session_code}).first()

        if session_relacion is None:
            return response.status(402)

        session = session_relacion.serialize()

        lapso = (datetime.now() - datetime.combine(datetime.now(), session["inicio"])).seconds

        if lapso > 7200:
            Session.where({"id": session["id"]}).delete()
            return response.status(402)

        if lapso > 6600:
            Session.where({"id": session["id"]}).delete()
            Session.create(
                {"curp": session["curp"], "session": session_code, "inicio": datetime.now()}
            )
        return request

    def after(self, request, response):
        return request
