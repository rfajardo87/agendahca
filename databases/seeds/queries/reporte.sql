/*
-- Copyright (C) 2023 Rubén de Jesús Fajardo Jaime
--
-- Este programa es software libre: puedes redistribuirlo y/o modificarlo
-- bajo los términos de la Licencia Pública General de GNU tal como está
-- publicada por la Fundación para el Software Libre, ya sea la versión 3
-- de la Licencia, o (a tu elección) cualquier versión posterior.
--
-- Este programa se distribuye con la esperanza de que sea útil, pero
-- SIN GARANTÍA ALGUNA; sin siquiera la garantía implícita de
-- COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Véase la
-- Licencia Pública General de GNU para más detalles.
--
-- Debes haber recibido una copia de la Licencia Pública General de GNU
-- junto con este programa. Si no, consulta <https://www.gnu.org/licenses/>.
*/

CREATE VIEW reporte AS
SELECT
  m.fecha,
  m.total,
  i.total inicial,
  f.total asistencia,
  n.total inasistencia,
  r.total reagendar,
  o.total reagendadas,
  p.total pv,
  s.total subsecuentes,
  pa.total pv_asistencia,
  sa.total ss_asistencia,
  pf.total pv_inasistencia,
  sf.total ss_inasistencia
FROM
  fn_reporte() m -- conteo mensual
  LEFT JOIN fn_reporte('ini') i --conteo status inicial
    ON m.fecha = i.fecha
  LEFT JOIN fn_reporte('fin') f --conteo finalizado
    ON m.fecha = f.fecha
  LEFT JOIN fn_reporte('nfn') n --conteo no fializadas
    ON m.fecha = n.fecha
  LEFT JOIN fn_reporte('rea') r --conteo por reagendar
    ON m.fecha = r.fecha
  LEFT JOIN fn_reporte('reo') o --conte citas ya reagendadas
    ON m.fecha = o.fecha
  LEFT JOIN fn_reporte('',false,0) p --conteo primera vez
    ON m.fecha = p.fecha
  LEFT JOIN fn_reporte('',true,0) s -- conteo subsecuentes
    ON m.fecha = s.fecha
  LEFT JOIN fn_reporte('fin',false,0) pa --conteo primera vez asistencia
    ON m.fecha = pa.fecha
  LEFT JOIN fn_reporte('fin',true,0) sa --conteo subsecuente asistencia
    ON m.fecha = sa.fecha
  LEFT JOIN fn_reporte('nfn',false,0) pf -- conteo primera vez falta
    ON m.fecha = pf.fecha
  LEFT JOIN fn_reporte('nfn',true,0) sf -- conteo subsecuente falta
    ON m.fecha = sf.fecha;

