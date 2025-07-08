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

CREATE VIEW horario_template AS
SELECT
  concat('"',
    concat_ws('","',
      h1.issub,
      h1.hora,
      h2.issub,
      h2.hora
    ),
    '"') fila
FROM
  (
	SELECT
	  row_number() over () ref,
	  hora,
	CASE WHEN issub THEN '' ELSE 'primera' END issub
	FROM
	  horarios
	WHERE
	  fecha = '2025-01-01'
  ) h1
LEFT JOIN (
	SELECT
	  row_number() over () ref,
	  hora,
	CASE WHEN issub THEN '' ELSE 'primera' END issub
	FROM
	  horarios
	WHERE
	  fecha = '2025-01-02'
) h2
ON h1.ref = h2.ref;
