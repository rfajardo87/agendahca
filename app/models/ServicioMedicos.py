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

"""ServicioMedicos Model"""

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class ServicioMedicos(Model):
    """ServicioMedicos Model"""

    __table__ = "servicio_medicos"
    __timezone__ = "America/Mexico_City"

    @belongs_to("servicio", "id")
    def servicios(
        self,
    ):
        from app.models.Servicio import Servicio

        return Servicio

    @belongs_to("curp", "curp")
    def medico(
        self,
    ):
        from app.models.Empleado import Empleado

        return Empleado
