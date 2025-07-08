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

"""PerfilComponentTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.PerfilComponente import PerfilComponente


class PerfilComponentTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        rels = [
            {"perfil": 1, "componente": 2},
            {"perfil": 1, "componente": 3},
            {"perfil": 1, "componente": 4},
            {"perfil": 1, "componente": 5},
            {"perfil": 1, "componente": 6},
            {"perfil": 1, "componente": 7},
            {"perfil": 1, "componente": 8},
        ]

        PerfilComponente.bulk_create(rels)
