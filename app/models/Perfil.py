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

"""Perfil Model"""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Perfil(Model):
    """Perfil Model"""

    __timezone__ = "America/Mexico_City"
    __table__ = "perfiles"

    @has_many("id", "perfil")
    def seguridad(
        self,
    ):
        from app.models.Seguridad import Seguridad

        return Seguridad

    @has_many("id", "perfil")
    def componentes(
        self,
    ):
        from app.models.PerfilComponente import PerfilComponente

        return PerfilComponente
