from django.test import TestCase

# Create your tests here.
class myTest(TestCase):
    def test_my_first_test(self):
        self.assertEqual(1,1)