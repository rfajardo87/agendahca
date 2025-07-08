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

"""QueriesTableSeeder Seeder."""

from masoniteorm.query import QueryBuilder
from masoniteorm.seeds import Seeder

from app.models.Query import Query
from app.models.Tipo import Tipo


class QueriesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        if Tipo.all().count() < 1:
            Tipo.create({"id": "Qry", "tipo": "Query"})
            Tipo.create({"id": "Vw", "tipo": "Vista"})
            Tipo.create({"id": "Fn", "tipo": "Funcion"})

        archivos = [
            ["horario_template", "Vw"],
            ["v_citas", "Vw"],
            ["disponibles", "Qry"],
            ["fn_reporte", "Fn"],
            ["reporte", "Vw"],
            ["v_medicos", "Vw"],
        ]

        qrys = [q.nombre for q in Query.select(["nombre"]).all()]

        for archivo in archivos:
            nombre = archivo[0]
            if nombre in qrys:
                continue
            with open(f"./databases/seeds/queries/{nombre}.sql", "r") as file:
                content = file.read()
                Query.create(
                    {
                        "nombre": nombre,
                        "query": content,
                        "tipo": archivo[1],
                    }
                )

        ejecutar = Query.where_in("tipo", ["Vw","Fn"]).where("exec", False).all().serialize()

        builder = QueryBuilder()

        for cmd in ejecutar:
            qry = cmd["query"]
            builder.statement(qry)

            Query.where({"nombre": cmd["nombre"]}).update({"exec": True})
