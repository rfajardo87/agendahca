from icecream import ic

from tests.TestCase import TestCase


class EmpleadoTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_route_exists(
        self,
    ):
        self.assertTrue(self.get("/empleado"))

    def test_route_200(
        self,
    ):
        self.get("/empleado").assertIsStatus(200)

    def test_filter(
        self,
    ):
        response = self.get("/empleado/adm")
        datos = response.response
        ic(datos)
        # response.assertOk()

    def test_filter_not_found(
        self,
    ):
        self.get("/empleado/juv").assertOk()
