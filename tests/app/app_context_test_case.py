import unittest

from app.setup import create_app
from tests import settings

class AppContextTestCase(unittest.TestCase):
    """
    unittest.TestCase that creates a Flask app context on setUp
    and destroys it on tearDown
    """
    def setUp(self):
        self._app = create_app(settings)
        self._app_context = self._app.app_context()
        self._app_context.push()

    def tearDown(self):
        self._app_context.pop()

    def test_request_context(self, *args, **kwargs):
        return self._app.test_request_context(*args, **kwargs)
