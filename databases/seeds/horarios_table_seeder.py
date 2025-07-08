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

"""HorariosTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.Empleado import Empleado
from app.models.Horario import Horario


class HorariosTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        emp = Empleado.where("curp", "admin").first()

        horarios = [
            {
                "fecha": "2025-01-01",
                "hora": "08:00",
                "issub": False,
            },
            {
                "fecha": "2025-01-01",
                "hora": "08:40",
                "issub": False,
            },
            {
                "fecha": "2025-01-01",
                "hora": "09:20",
                "issub": True,
            },
            {
                "fecha": "2025-01-02",
                "hora": "09:40",
                "issub": True,
            },
            {
                "fecha": "2025-01-02",
                "hora": "10:00",
                "issub": True,
            },
        ]
        lst_horarios = [
            {**h, "curp": emp["curp"], "isdefault": True, "isaut": True} for h in horarios
        ]

        Horario.bulk_create(lst_horarios)
