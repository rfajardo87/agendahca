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

from routes.cita import CITA_ROUTES
from routes.components import COMPONENT_ROUTES
from routes.empleado import EMPLEADO_ROUTES
from routes.paciente import PACIENTE_ROUTES
from routes.reportes import REPORTE_ROUTES
from routes.solicitud import SOLICITUD_ROUTES
from routes.template import TEMPLATE_ROUTES

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.post("/session", "WelcomeController@session"),
    Route.post("/checksession", "WelcomeController@verify_active"),
    Route.post("/cerrar", "WelcomeController@cerrar_session"),
    *EMPLEADO_ROUTES,
    *PACIENTE_ROUTES,
    *SOLICITUD_ROUTES,
    *CITA_ROUTES,
    *TEMPLATE_ROUTES,
    *REPORTE_ROUTES,
    *COMPONENT_ROUTES,
]
