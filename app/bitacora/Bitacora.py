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

import logging

from .BitacoraHandler import BitacoraHandler


class Bitacora:

    def __init__(self, level=logging.DEBUG):
        super().__init__()
        self.logg = logging.Logger("main")
        self.logg.setLevel(level)
        customHndlr = BitacoraHandler()
        self.logg.addHandler(customHndlr)

    def debug(self, kwargs):
        self.logg.debug(kwargs=kwargs)

    def info(self, kwargs):
        self.logg.info("informacion", kwargs=kwargs)

    def warning(self, kwargs):
        self.logg.warning(kwargs=kwargs)

    def error(self, kwargs):
        self.logg.error(kwargs=kwargs)

    def critical(self, kwargs):
        self.logg.critical(kwargs=kwargs)
