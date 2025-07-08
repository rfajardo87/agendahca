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

from masonite.routes import Route

CITA_ROUTES = [
    Route.group(
        [
            Route.post("/", "CitaController@create"),
            Route.get("/@curp", "CitaController@citas"),
            Route.get("/@curp/agenda/@ano/@mes", "CitaController@agenda"),
            Route.get("/@curp/mensual/@ano/@mes", "CitaController@mensual"),
            Route.get("/@curp/disponibles/@ano/@mes", "CitaController@disponibles"),
        ],
        prefix="/cita",
        name="cita",
    ),
    Route.get("/citacolor", "CitaController@color"),
    Route.put("/finalizar/@id/@estado", "CitaController@finalizar"),
]
