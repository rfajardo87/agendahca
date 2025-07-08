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

from app.models.Autorizacion import Autorizacion
from app.models.Horario import Horario
from app.models.TemplateHorario import TemplateHorario


class TemplateController(Controller):
    def horarios(self, response: Response):
        try:
            filas = [f'{f["fila"]}\n' for f in TemplateHorario.all()]
            filas_temp = [f'"","2025-01-01","","2025-01-02"\n', *filas]
            file_name = "reports/plantilla_horarios.csv"
            with open(file_name, "w") as f:
                f.writelines(filas_temp)
            return response.download("plantilla_horarios", file_name, force=True)
        except Exception as e:
            return str(e)

    def cargar(self, request: Request, response: Response):
        try:
            data = request.all()
            empleado = request.param("empleado")

            contenido = data["archivoContent"].replace('"', "").split("\n")

            horarios = []
            autorizacion = (
                Autorizacion.joins("peticion")
                .where("peticion.tipo", "horarios")
                .select("valor")
                .first()
            )

            fila1 = contenido[0].split(",")
            fechas = fila1[1::2]
            filas = [fila.split(",") for fila in contenido[1:]]
            for fila in filas:
                if len(fila) < 2:
                    continue
                tipos = fila[::2]
                horas = fila[1::2]
                indice = -1
                for hora in horas:
                    indice += 1
                    if not hora:
                        continue
                    horarios.append(
                        {
                            "curp": empleado,
                            "fecha": fechas[indice],
                            "hora": hora,
                            "isdefault": False,
                            "isaut": autorizacion.valor,
                            "issub": False if tipos[indice] == "primera" else True,
                        }
                    )
            Horario.bulk_create(horarios)
            return response.status(200)
        except Exception as e:
            return str(e)
