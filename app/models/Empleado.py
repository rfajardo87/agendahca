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

"""Empleado Model"""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many, has_one


class Empleado(Model):
    """Empleado Model"""

    __timezone__ = "America/Mexico_City"
    __primary__ = "curp"

    @has_many("curp", "empleado")
    def dias(
        self,
    ):
        from app.models.Dia import Dia

        return Dia

    @has_many("curp", "empleado")
    def observaciones(
        self,
    ):
        from app.models.Solicitud import Solicitud

        return Solicitud

    @has_many("curp", "curp")
    def servicios(
        self,
    ):
        from app.models.ServicioMedicos import ServicioMedicos

        return ServicioMedicos

    @has_many("curp", "medico")
    def citas(
        self,
    ):
        from app.models.Cita import Cita

        return Cita

    @has_many("curp", "curp")
    def horarios(
        self,
    ):
        from app.models.Horario import Horario

        return Horario

    @has_one("curp", "curp")
    def accesso(
        self,
    ):
        from app.models.Seguridad import Seguridad

        return Seguridad

    @has_many("curp", "curp")
    def session(
        self,
    ):
        from app.models.Session import Session

        return Session
