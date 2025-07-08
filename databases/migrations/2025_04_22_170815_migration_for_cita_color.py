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

"""MigrationForCitaColor Migration."""

from masoniteorm.migrations import Migration


class MigrationForCitaColor(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("code") as table:
            table.increments("id")
            table.string("codigo")
            table.string("descripcion")

        with self.schema.create("color") as table:
            table.integer("id")
            table.integer("code")
            table.string("main",length=7)
            table.string("container",length=7)
            table.string("onContainer",length=7)
            table.boolean("activo").default(True)

            table.foreign("code").references("id").on("code").on_update("cascade").on_delete("restrict")

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("color")
        self.schema.drop("code")
