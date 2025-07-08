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

"""ComponentsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.Componente import Componente


class ComponentsTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        components = [
            {"nombre": "App", "padre": None, "ruta": None, "activo": True, "orden": 1, "tab": 0},
            {
                "nombre": "Control",
                "padre": 1,
                "ruta": "control",
                "activo": True,
                "orden": 2,
                "tab": 0,
            },
            {
                "nombre": "Medico",
                "padre": 2,
                "ruta": "selector",
                "activo": True,
                "orden": 1,
                "tab": 0,
            },
            {
                "nombre": "Paciente",
                "padre": 2,
                "ruta": "selector",
                "activo": True,
                "orden": 2,
                "tab": 1,
            },
            {"nombre": "Nuevo", "padre": 2, "ruta": "nuevo", "activo": True, "orden": 3, "tab": 1},
            {
                "nombre": "Historial",
                "padre": 2,
                "ruta": None,
                "activo": False,
                "orden": 5,
                "tab": 2,
            },
            {
                "nombre": "Navmin",
                "padre": None,
                "ruta": "navmin",
                "activo": True,
                "orden": 1,
                "tab": 0,
            },
            {"nombre": "Fecha", "padre": 2, "ruta": "fecha", "activo": True, "orden": 4, "tab": 2},
            {
                "nombre": "Plantilla",
                "padre": 2,
                "ruta": "template",
                "activo": True,
                "orden": 5,
                "tab": 1,
            },
            {
                "nombre": "Recargar",
                "padre": 2,
                "ruta": "recargar",
                "activo": True,
                "orden": 6,
                "tab": 0,
            },
        ]

        Componente.bulk_create(components)
