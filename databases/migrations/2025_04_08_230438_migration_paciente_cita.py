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

"""MigrationPacienteCita Migration."""

from masoniteorm.migrations import Migration


class MigrationPacienteCita(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("pacientes") as table:
            table.string("curp",length=30).unique().primary()
            table.string("expediente",length=30).nullable()
            table.string("nombre")
            table.string("contacto")
            table.string("domicilio").nullable()
            table.date("nacimiento").nullable()
            table.boolean("genero").default(True)

            table.timestamps()

        with self.schema.create("citas") as table:
            table.increments("id")
            table.string("paciente",length=30)
            table.string("medico",length=30)
            table.date("fecha")
            table.time("hora")
            table.small_integer("servicio").nullable()
            table.boolean("issub").default(True)

            table.timestamps()
            table.soft_deletes()

            table.foreign("paciente").references("curp").on("pacientes").on_delete("restrict").on_update("cascade")
            table.foreign("medico").references("curp").on("empleados").on_update("cascade").on_delete("restrict")
            table.foreign("servicio").references("id").on("servicios").on_update("cascade").on_delete("restrict")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("citas")
        self.schema.drop("pacientes")
