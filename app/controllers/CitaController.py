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

import calendar
from datetime import datetime
from icecream import ic
import pdb

from config.database import DB

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from masoniteorm.query import QueryBuilder

from app.models.Cita import Cita
from app.models.CitaColor import Color
from app.models.Dia import Dia
from app.models.Empleado import Empleado
from app.models.Horario import Horario
from app.models.Paciente import Paciente
from app.models.Query import Query
from app.models.Servicio import Servicio
from app.models.Status import Status
from app.models.VCita import VCita


class CitaController(Controller):
    def show(self, view: View):
        return view.render("welcome")

    def create(self, request: Request, response: Response):
        try:
            cita = request.all()
            medico_id = str(cita["medico"])
            medico_qry = (
                Empleado.joins("servicios", clause="left")
                .where("curp", medico_id)
                .where("medico", True)
                .select_raw("servicio_medicos.servicio id")
            )

            servicio_db = medico_qry.all()
            if servicio_db.is_empty():
                raise Exception("Medico no registrado")

            if ("servicio" not in cita.keys()) or servicio_db.where(
                "id", cita["servicio"]
            ).is_empty():
                db_servicio = servicio_db.first().serialize()
                cita["servicio"] = db_servicio["id"]

            fecha_disponible = (
                Dia.where("empleado", medico_id).where("dia", str(cita["fecha"])).all().is_empty()
            )
            if not fecha_disponible:
                raise Exception("Fecha no disponible")

            paciente_dexists = Paciente.where("curp", str(cita["paciente"])).all().is_empty()
            if paciente_dexists:
                raise Exception("Paciente no registrado")

            with DB.transaction():

                condiciones = {"medico": medico_id, "paciente": str(cita["paciente"])}
                Cita.where({**condiciones, "status": "rea"}).update({"status": "reo"})

                Cita.where({**condiciones, "status": "reo"}).delete()

                cita = Cita.create(cita).fresh()
                ic(cita)

            response.status(201)
            return VCita.where("id", cita["id"]).first()
        except Exception as e:
            return str(e)

    def citas(self, request: Request, response: Response):
        try:
            curp = request.param("curp")
            vcitas = (
                VCita.where("curp", curp)
                .where("fecha", ">=", f"{datetime.now().year}-01-01")
                .order_by("fecha", "asc")
                .order_by("inicio", "asc")
                .all()
            )

            return vcitas
        except Exception as e:
            return str(e)

    def agenda(self, request: Request, response: Response):
        try:
            curp = request.param("curp")
            mes = request.param("mes")
            ano = request.param("ano")
            where_ano = f"EXTRACT(YEAR FROM fecha::date) = {ano}"
            where_mes = f"EXTRACT(MONTH FROM fecha::date) = {mes}"
            citas = VCita.where("curp", curp).where_raw(where_ano).where_raw(where_mes)

            return citas.all()
        except Exception as e:
            return str(e)

    def color(
        self,
    ):
        try:
            return Color.joins("code").all()
        except Exception as e:
            return str(e)

    def dias_event(self, evento):
        comision = evento["comision"]
        return {
            **evento,
            "calendarId": "com" if comision else "aus",
            "title": "Comision" if comision else "Ausente",
        }

    def mensual(self, request: Request, response: Response):
        try:
            empleado = request.param("curp")
            mes = request.param("mes")
            ano = request.param("ano")
            where_ano = f"EXTRACT(YEAR FROM fecha) = {ano}"
            where_mes = f"EXTRACT(MONTH FROM fecha) = {mes}"
            fuera = (
                Dia.where("empleado", empleado)
                .where("isaut", True)
                .where_raw(f"EXTRACT(YEAR FROM dia) = {ano}")
                .where_raw(f"EXTRACT(MONTH FROM dia) = {mes}")
                .select_raw("dia::varchar fecha")
                .select(["comision"])
                .all()
                .serialize()
            )

            fuera_lst = [self.dias_event(f) for f in fuera]

            asignadas = (
                Cita.where("medico", empleado)
                .where_raw(where_ano)
                .where_raw(where_mes)
                .group_by("fecha")
                .select_raw("fecha::varchar fecha")
                .all()
                .serialize()
            )

            asignadas_lst = [
                {**asignada, "calendarId": "cita", "title": "Citas"} for asignada in asignadas
            ]
            return [*fuera_lst, *asignadas_lst]
        except Exception as e:
            return str(e)

    def map_event(self, evento, isManual=True, isDisponible=True):
        issub = evento["issub"]
        if isManual:
            issub = evento["issub"] == "true"
        calendarId = "ss" if issub else "pv"
        if isDisponible:
            calendarId += "_d"
        return {
            **evento,
            "issub": issub,
            "title": "Subsecuente" if issub else "Primera vez",
            "calendarId": calendarId,
        }

    def disponibles(self, request: Request, reponse: Response):
        try:
            curp = str(request.param("curp"))
            ano = request.param("ano")
            mes = request.param("mes")

            horarios = (
                Horario.where("curp", curp)
                .where_raw(f"EXTRACT(YEAR FROM fecha)={ano}")
                .where_raw(f"EXTRACT(MONTH FROM fecha)={mes}")
                .select(["issub"])
                .select_raw("fecha::varchar,hora::varchar")
                .all()
                .serialize()
            )

            horarios_lst = [self.map_event(x, False) for x in horarios]

            builder = QueryBuilder()

            ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
            fecha = f"{ano}-{mes}-{ultimo_dia}"
            qry = Query.where("nombre", "disponibles").first().serialize()
            omision = builder.statement(qry["query"], [str(curp), str(fecha)])

            omision_lst = [dict(o) for o in omision]
            omision_agenda = map(self.map_event, omision_lst)

            return [*horarios_lst, *omision_agenda]
        except Exception as e:
            return str(e)

    def finalizar(self, request: Request, response: Response):
        try:
            id = request.param("id")
            estado = request.param("estado")
            status = Status.where_in("status", ["Inicial", "Finalizado"]).where("id", estado)

            if status.all().is_empty():
                raise Exception("Status no valido")

            Cita.where({"id": id}).update({"status": estado})

            return response.status(200)
        except Exception as e:
            return str(e)
