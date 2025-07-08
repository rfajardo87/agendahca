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

"""PerfilTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.Perfil import Perfil


class PerfilTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        Perfil.create({"perfil": "admin"})
        Perfil.create({"perfil": "medico"})
        Perfil.create({"perfil": "caja"})
        Perfil.create({"perfil": "coordinacion"})
        Perfil.create({"perfil": "archivo"})
        Perfil.create({"perfil": "enfermeria"})
        Perfil.create({"perfil": "direccion"})
        Perfil.create({"perfil": "sysadmin"})
