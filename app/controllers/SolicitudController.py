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

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Solicitud import Solicitud


class SolicitudController(Controller):
    def show(self, request: Request, response: Response):
        try:
            emp = request.param("emp")
            year = request.param("year")
            mes = request.param("mes")
            where_year = f"EXTRACT(year from created_at) = {str(year)}"
            where_mes = f"EXTRACT(month from created_at) = {str(mes)}"
            solicitudes = (
                Solicitud.where("empleado", str(emp))
                .where_raw(where_year)
                .where_raw(where_mes)
                .select(["observacion", "created_at"])
                .order_by("created_at", "desc")
                .all()
                .take(5)
            )

            return solicitudes
        except Exception as e:
            return str(e)

    def create(self, request: Request, response: Response):
        try:
            emp = request.param("emp")
            data = request.only("observacion")
            solicitud = Solicitud.create(
                {
                    "empleado": emp,
                    "observacion": data["observacion"],
                }
            ).fresh()
            response.status(201)
            return solicitud
        except Exception as e:
            return str(e)
