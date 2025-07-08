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

"""CitaColorTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.CitaColor import Color
from app.models.Code import Code


class CitaColorTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        tipos = [
            ["ss", "subsecuente"],
            ["pv", "primera vez"],
            ["ss_d", "subsecuente disponible"],
            ["pv_d", "primera vez disponible"],
            ["aus", "dias de ausencia"],
            ["com", "dias de comision"],
            ["cita", "dias en el mes con cita programadas"],
            ["rag", "necesita reagendar"],
        ]

        tipo_bulk = [{"codigo": t[0], "descripcion": t[1]} for t in tipos]

        Code.bulk_create(tipo_bulk)

        colors = [
            {
                "id": 1,
                "main": "#FF7EE2",
                "container": "#FDB7EA",
                "onContainer": "#000",
            },
            {
                "id": 2,
                "main": "#FF9900",
                "container": "#FFD699",
                "onContainer": "#000",
            },
            {
                "id": 3,
                "main": "#258e25",
                "container": "#c2efc2",
                "onContainer": "#000",
            },
            {
                "id": 4,
                "main": "#1a8cff",
                "container": "#b3d9ff",
                "onContainer": "#000",
            },
            {
                "id": 5,
                "main": "#FF0000",
                "container": "#FFB3B3",
                "onContainer": "#000",
            },
            {
                "id": 6,
                "main": "#F9E400",
                "container": "#F2E2B1",
                "onContainer": "#000",
            },
            {
                "id": 7,
                "main": "#A594F9",
                "container": "#E5D9F2",
                "onContainer": "#000",
            },
            {
                "id": 8,
                "main": "#EA047E",
                "container": "#D14787",
                "onContainer": "#FEFEFE",
            },
        ]

        colores = [{**color, "code": color["id"]} for color in colors]

        Color.bulk_create(colores)
