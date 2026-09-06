import unittest

from app import app


class ApiRouteTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_index_lists_public_routes(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"/courses", response.data)
        self.assertIn(b"/resume", response.data)

    def test_courses_returns_json(self) -> None:
        response = self.client.get("/courses")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response.get_json(), (dict, list))

    def test_missing_route_uses_the_404_template(self) -> None:
        response = self.client.get("/does-not-exist")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
