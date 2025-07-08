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

"""MigrationForComponentPerfil Migration."""

from masoniteorm.migrations import Migration


class MigrationForComponentPerfil(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("perfil_components") as table:
            table.increments("id")
            table.integer("perfil")
            table.integer("componente")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("perfil_components")
