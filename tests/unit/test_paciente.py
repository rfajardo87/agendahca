from tests.TestCase import TestCase


class PacienteTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_route_exists(
        self,
    ):
        self.assertTrue(self.get("/paciente"))

    def test_route_get_ok(
        self,
    ):
        self.get("/paciente").assertOk()
