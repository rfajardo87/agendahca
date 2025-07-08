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

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masoniteorm.query import QueryBuilder

from app.models.Query import Query


class ReportesController(Controller):
    def show(self, request: Request, response: Response):
        try:
            mes = request.param("mes")
            qb = QueryBuilder()
            qry = Query.where("nombre", "reporte").first().serialize()
            registros = qb.statement(qry["query"], [mes])
            datos = [
                ",".join(
                    [
                        "PACIENTE",
                        "MEDICO",
                        "FECHA",
                        "INICIO",
                        "FIN",
                        "SERVICIO",
                        "STATUS",
                        "TIPO",
                        "GRUPO",
                    ]
                ),
                *[",".join(list(registro.values())) for registro in registros],
            ]
            filas = [f"{dato}\n" for dato in datos]
            file_name = f"reports/reporte{mes}.csv"
            with open(file_name, "w") as f:
                f.writelines(filas)
            return response.download(f"mensual{mes}", file_name, force=True)
        except Exception as e:
            return str(e)
