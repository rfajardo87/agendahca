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

"""MigrationForSolicitudes Migration."""

from masoniteorm.migrations import Migration


class MigrationForSolicitudes(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("solicitudes") as table:
            table.increments("id")
            table.string("empleado",length=30)
            table.text("observacion")
            table.timestamps()

            table.index("empleado")

            table.foreign('empleado').references('curp').on('empleados').on_update('cascade').on_delete('restrict')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("solicitudes")
