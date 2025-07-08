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

"""MigrationForStatusCita Migration."""

from masoniteorm.migrations import Migration


class MigrationForStatusCita(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("status") as table:
            table.string("id",length=3).primary()
            table.string("status",length=15)
            table.string("color",length=7)

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("status")
