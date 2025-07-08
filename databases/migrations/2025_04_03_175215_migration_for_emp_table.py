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

"""MigrationForEmpTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForEmpTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("empleados") as table:
            table.string("curp",length=30).primary().unique()
            table.string("nombre")
            table.string("contacto")
            table.boolean("medico").nullable().default(False)
            table.boolean("turno").nullable().default(True)

            table.timestamps()
            table.soft_deletes()

        with self.schema.create("perfiles") as table:
            table.increments("id")
            table.string("perfil",length=50)

            table.timestamps()

        with self.schema.create("seguridad") as table:
            table.string("curp",length=30).primary()
            table.string("contra")
            table.integer("perfil")

            table.timestamps()

            table.foreign("curp").references("curp").on("empleados").on_update("cascade").on_delete("restrict")
            table.foreign("perfil").references("id").on("perfiles").on_update("cascade").on_delete("restrict")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("seguridad")
        self.schema.drop("empleados")
        self.schema.drop("perfiles")
