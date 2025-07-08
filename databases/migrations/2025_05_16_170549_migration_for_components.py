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

"""MigrationForComponents Migration."""

from datetime import datetime

from masoniteorm.migrations import Migration


class MigrationForComponents(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("components") as table:
            table.increments("id")
            table.string("nombre")
            table.integer("padre").nullable()
            table.string("ruta").nullable()
            table.boolean("activo").default(True)
            table.integer("orden")
            table.integer("tab").default(0)

            table.timestamps()

            table.foreign("padre").references("id").on("components").on_delete("restrict").on_delete("cascade")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("components")
