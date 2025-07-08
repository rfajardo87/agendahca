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

from masonite.routes import Route

EMPLEADO_ROUTES = [
    Route.group(
        [
            Route.get("/?filtro", "EmpleadoController@show"),
            Route.post("/@emp/dia/@dia", "EmpleadoController@addDay"),
            Route.delete("/@emp/dia/@dia", "EmpleadoController@rmDay"),
            Route.get("/@emp/calendar/@anno/@mes", "EmpleadoController@dias"),
            Route.get("/@emp/agenda/@start/@end", "EmpleadoController@list_week"),
        ],
        prefix="/empleado",
        name="empleado",
    ),
    Route.get("/medico/?filtro", "EmpleadoController@medicos"),
    Route.get("/component", "EmpleadoController@component"),
    Route.get("/qr/@curp", "EmpleadoController@qr_access"),
]
