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

"""StatusTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.Status import Status


class StatusTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        status_lst = [
            {"id": "ini", "status": "Inicial", "color": "#CDC1FF"},
            {"id": "fin", "status": "Finalizado", "color": "#95BDFF"},
            {"id": "nfn", "status": "No Finalizado", "color": "#FF3F33"},
            {"id": "rea", "status": "Reasignar", "color": "#FF9F00"},
            {"id": "reo", "status": "Reasignado", "color": "#A6AEBF"},
            {"id": "prg", "status": "En Progreso", "color": "#A5DD9B"},
        ]

        Status.bulk_create(status_lst)
