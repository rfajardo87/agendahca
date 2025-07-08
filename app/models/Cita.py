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

"""Cita Model"""

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many
from masoniteorm.scopes import SoftDeletesMixin


class Cita(Model, SoftDeletesMixin):
    """Cita Model"""

    __timezone__ = "America/Mexico_City"
    __table__ = "citas"

    @belongs_to("paciente", "expediente")
    def paciente(
        self,
    ):
        from app.models.Paciente import Paciente

        return Paciente

    @belongs_to("medico", "curp")
    def medico(
        self,
    ):
        from app.models.Empleado import Empleado

        return Empleado

    @belongs_to("servicio", "id")
    def servicio(
        self,
    ):
        from app.models.Servicio import Servicio

        return Servicio

    @belongs_to("status", "id")
    def status(
        self,
    ):
        from app.models.Status import Status

        return Status

    @has_many("id", "cita")
    def observaciones(
        self,
    ):
        from app.models.Solicitud import Solicitud

        return Solicitud
