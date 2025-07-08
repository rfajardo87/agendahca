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

CREATE OR REPLACE FUNCTION fn_reporte(state varchar(3) = '', grupo boolean = true, banderaGrpGral INTEGER  = 1)
RETURNS TABLE(total INTEGER, fecha DATE)
LANGUAGE plpgsql
AS $$
  BEGIN
    IF state = '' THEN
      RETURN QUERY
      SELECT
        COUNT(c.fecha)::INTEGER,
        c.fecha::DATE
      FROM
        citas c
      WHERE
        c.issub = grupo
        OR
        banderaGrpGral = 1
      GROUP BY
        c.fecha;
    END IF;

    RETURN QUERY
    SELECT
      COUNT(c.fecha)::INTEGER,
      c.fecha::DATE
    FROM
      citas c
    WHERE
      c.status = state
      AND
      (
        c.issub = grupo
        OR
        banderaGrpGral = 1
      )
    GROUP BY
      c.fecha;
  END;
$$;
