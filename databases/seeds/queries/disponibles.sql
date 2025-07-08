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

WITH gen AS (
	SELECT 
	  g.fecha::date,
	  h.hora::time,
	  h.issub,
	  '?' curp
	FROM 
	  (
		SELECT generate_series(now()::date,'?'::date,interval '1 day') fecha
	  ) g
	  CROSS JOIN horarios h
	WHERE h.isdefault
)
SELECT 
  gen.fecha::varchar fecha,
  gen.hora::varchar hora,
  gen.issub::varchar issub
FROM
  gen
  LEFT JOIN dias d on gen.fecha = d.dia and gen.curp = d.empleado
  LEFT JOIN horarios h on gen.fecha = h.fecha and gen.curp = h.curp
  LEFT JOIN citas c on gen.fecha = c.fecha and gen.hora = c.hora and gen.curp = c.medico
WHERE
  d.dia IS NULL
  AND
  h.fecha IS NULL
  AND
  c.fecha IS NULL;
