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

"""A WelcomeController Module."""

from datetime import datetime

import pyotp
from masonite.controllers import Controller
from masonite.facades import Hash
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Empleado import Empleado
from app.models.Log import Log
from app.models.PerfilComponente import PerfilComponente
from app.models.Seguridad import Seguridad
from app.models.Session import Session


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("index")

    def session(self, request: Request, response: Response):
        try:
            pss = str(request.input("pss"))

            segs = (
                Seguridad.joins("perfil")
                .select(["curp", "contra"])
                .select_raw("perfiles.perfil perfil")
                .select_raw("perfiles.id perfil_id")
                .all()
                .serialize()
            )

            for seg in segs:
                totp = pyotp.TOTP(seg["contra"])
                if totp.verify(pss):
                    Session.where({"curp": seg["curp"]}).delete()
                    session_hash = Hash.make(f"{seg['curp']}{totp.now()}")
                    Session.create(
                        {
                            "session": session_hash,
                            "curp": seg["curp"],
                            "inicio": datetime.now(),
                        }
                    )

                    is_app = (
                        PerfilComponente.where({"perfil": seg["perfil_id"], "componente": 1})
                        .all()
                        .is_empty()
                    )

                    seg["contra"] = None
                    Log.create(
                        {
                            "curp": seg["curp"],
                            "ruta": "/session",
                            "metodo": "POST",
                            "fecha": datetime.now(),
                            "datos": f"{seg}",
                            "level": "info",
                        }
                    )

                    return {
                        **seg,
                        "contra": None,
                        "entry": None if is_app else "App",
                        "session": session_hash,
                    }

            return response.status(403)
        except Exception as e:
            return str(e)

    def verify_active(self, request: Request, response: Response):
        try:
            session = request.input("session")

            activa = Session.where({"session": session}).all()

            if activa.is_empty():
                return response.status(401)

            session_valida = activa.first()

            session_activa = session_valida.serialize()
            tiempo_activo = datetime.now() - datetime.combine(
                datetime.now(), session_activa["inicio"]
            )

            if tiempo_activo.seconds > 60 * 60 * 2:
                return response.status(401)

            curp = session_activa["curp"]
            data = (
                Seguridad.joins("perfil")
                .where({"curp": curp})
                .select_raw("perfiles.perfil perfil")
                .select_raw("perfiles.id perfil_id")
                .select("curp")
                .first()
                .serialize()
            )

            is_app = (
                PerfilComponente.where({"perfil": data["perfil_id"], "componente": 1})
                .all()
                .is_empty()
            )

            entry = None if is_app else "App"

            return {**data, "entry": entry, "session": session}
        except Exception as e:
            return str(e)

    def cerrar_session(self, request: Request, response: Response):
        try:
            session = request.header("session")

            Session.where("session", session).delete()

            return response.status(204)
        except Exception as e:
            return str(e)
