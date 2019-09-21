from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestApps(TestCase):
    def test_app(self):
        self.assertEqual('todo', TodoConfig.name)
        app_config = apps.get_app_config("todo")
        self.assertEqual("todo", app_config.label)
