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

"""Base Database Seeder Module."""

from masoniteorm.seeds import Seeder

from .autorizacion_table_seeder import AutorizacionTableSeeder
from .cita_color_table_seeder import CitaColorTableSeeder
from .components_table_seeder import ComponentsTableSeeder
from .empleado_table_seeder import EmpleadoTableSeeder
from .horarios_table_seeder import HorariosTableSeeder
from .perfil_component_table_seeder import PerfilComponentTableSeeder
from .perfil_table_seeder import PerfilTableSeeder
from .peticion_table_seeder import PeticionTableSeeder
from .queries_table_seeder import QueriesTableSeeder
from .seguridad_table_seeder import SeguridadTableSeeder
from .servicio_table_seeder import ServicioTableSeeder
from .status_table_seeder import StatusTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(CitaColorTableSeeder)
        self.call(PeticionTableSeeder)
        self.call(AutorizacionTableSeeder)
        self.call(PerfilTableSeeder)
        self.call(EmpleadoTableSeeder)
        self.call(ServicioTableSeeder)
        self.call(HorariosTableSeeder)
        self.call(QueriesTableSeeder)
        self.call(SeguridadTableSeeder)
        self.call(StatusTableSeeder)
        self.call(PerfilComponentTableSeeder)
        self.call(ComponentsTableSeeder)
