/*
-- Copyright (C) 2025 Rubén de Jesús Fajardo Jaime
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

CREATE VIEW v_citas AS
SELECT
  citas.id,
  pacientes.expediente,
  pacientes.nombre paciente,
  empleados.nombre medico,
  concat(citas.fecha,'') AS fecha,
  concat(citas.hora,'') AS inicio,
  concat(
    CASE WHEN citas.issub
    THEN citas.hora + interval '20 minutes'
    ELSE citas.hora + interval '40 minutes'
    END,''
  ) AS fin,
  servicios.nombre AS servicio,
  citas.issub,
  citas.status status_id,
  status.status,
  status.color,
  pacientes.curp curp_paciente,
  empleados.curp curp
FROM
  citas
  LEFT JOIN pacientes on citas.paciente = pacientes.curp
  LEFT JOIN empleados on citas.medico = empleados.curp
  LEFT JOIN servicios on citas.servicio = servicios.id
  LEFT JOIN status on citas.status = status.id
WHERE
  citas.deleted_at IS NULL;
