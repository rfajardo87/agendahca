# Copyright (C) 2025 Rubén de Jesús Fajardo Jaime
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

import uuid

from icecream import ic
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Paciente import Paciente


class PacienteController(Controller):
    def index(
        self,
    ):
        try:
            pacientes = (
                Paciente.select("*")
                .select_raw("nacimiento::varchar")
                .select_raw("created_at::varchar")
                .select_raw("updated_at::varchar")
                .all()
                .take(3)
                .serialize()
            )

            return pacientes
        except Exception as e:
            return str(e)

    def show(self, request: Request, response: Response):
        try:
            valor = request.param("exp")

            paciente = (
                Paciente.where("expediente", "like", f"%{valor}%")
                .or_where("curp", "like", f"%{valor}%")
                .or_where("nombre", "like", f"%{valor}%")
                .or_where("contacto", "like", f"%{valor}%")
                .select("*")
                .select_raw("nacimiento::varchar")
            )
            return paciente.get().serialize()
        except Exception as e:
            return str(e)

    def create(self, request: Request, response: Response):
        try:
            req = request.all()["data"]
            expediente = str(uuid.uuid4())[:30]
            if ("expediente" in req) and req["expediente"]:
                expedienete = req["expediente"]
            paciente = (
                Paciente.create(
                    {
                        **req,
                        "expediente": expediente,
                    }
                )
                .fresh()
                .serialize()
            )
            response.status(201)
            return paciente
        except Exception as e:
            return str(e)

    def update(self, request: Request, response: Response):
        try:
            # expediente = CURP
            expediente = request.param("exp")
            paciente = request.all()["data"]
            ic(paciente)
            ic(Paciente.where({"curp": expediente}).first())
            Paciente.where({"curp": expediente}).first().update(paciente)
            return response.status(204)
        except Exception as e:
            return str(e)
