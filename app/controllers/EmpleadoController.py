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

import base64
from icecream import ic
import pdb

import pyotp
import qrcode
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Autorizacion import Autorizacion
from app.models.Cita import Cita
from app.models.Dia import Dia
from app.models.Empleado import Empleado
from app.models.Seguridad import Seguridad
from app.models.Status import Status
from app.models.VMedicos import VMedicos
from config.database import DB


class EmpleadoController(Controller):
    def show(self, request: Request, response: Response):
        try:
            filtro = request.param("filtro")
            filtro_fmt = f"%{str(filtro)}%"
            if filtro:
                emp = Empleado.where("curp", "like", filtro_fmt).or_where(
                    "nombre", "like", filtro_fmt
                )

                return emp.all().take(3)
            return Empleado.all().take(3)
        except Exception as e:
            return str(e)

    def addDay(self, request: Request, response: Response):
        try:
            emp = request.param("emp")
            dia = request.param("dia")
            isComision = request.input("isComision")

            autorizacion = (
                Autorizacion.joins("peticion")
                .where("peticion.tipo", "dias")
                .select("valor")
                .first()
            )

            status = Status.where("id", "rea").first()
            with DB.transaction():
                ic(
                    Cita.where(
                        {
                            "medico": emp,
                            "fecha": dia,
                        }
                    ).update({"status": status["id"]})
                )

                dia = Dia.create(
                    {
                        "empleado": emp,
                        "dia": dia,
                        "isaut": autorizacion.valor,
                        "comision": isComision,
                    }
                ).fresh()

            fecha = f"{dia.dia}"

            response.status(201)
            return {
                "id": dia.id,
                "start": fecha,
                "end": fecha,
                "title": "Comision" if isComision else "Ausente",
                "calendarId": "com" if isComision else "aus",
            }
        except Exception as e:
            return str(e)

    def rmDay(self, request: Request, response: Response):
        try:
            emp = request.param("emp")
            dia = request.param("dia")

            dia = Dia.where(
                {
                    "empleado": emp,
                    "dia": dia,
                }
            )
            dia.delete()

            return response.status(200)
        except Exception as e:
            return str(e)

    def dias(self, request: Request, response: Response):
        try:
            emp = request.param("emp")
            anno = request.param("anno")
            mes = request.param("mes")
            where_anno = f"EXTRACT(year FROM dia) = {str(anno)}"
            where_mes = f"EXTRACT(month FROM dia) = {str(mes)}"
            dias_list = (
                Dia.where({"empleado": emp})
                .where_raw(where_anno)
                .where_raw(where_mes)
                .select(["id", "comision"])
                .select_raw("to_char(dia,'YYYY-MM-DD') dia")
            )
            rsp = dias_list.all().unique("dia")
            return rsp
        except Exception as e:
            return str(e)

    def medicos(self, request: Request, response: Response):
        try:
            filtro = request.param("filtro")
            medicos = (
                VMedicos.where("curp", "like", f"%{filtro}%").or_where(
                    "nombre", "like", f"%{filtro}%"
                )
                if filtro
                else VMedicos
            )

            return medicos.all().take(3)
        except Exception as e:
            return str(e)

    def list_week(self, request: Request, response: Response):
        try:
            medico = request.param("emp")
            inicio = request.param("start")
            fin = request.param("end")
            dias = (
                Dia.where("empleado", medico)
                .where_between("dia", inicio, fin)
                .select(["*"])
                .select_raw("to_char(dia, 'YYYY-MM-DD') dia")
            )

            return dias.all().unique("dia")
        except Exception as e:
            return str(e)

    def qr_access(self, request: Request, response: Response):
        try:
            curp = request.param("curp")
            seg = Seguridad.joins("empleado").where({"curp": curp}).get().serialize()

            nombre = seg[0]["nombre"]
            cadena = pyotp.totp.TOTP(seg[0]["contra"]).provisioning_uri(
                name=nombre, issuer_name="SiAHCA"
            )

            return cadena
        except Exception as e:
            return str(e)
