from django.test import TestCase

class SimpleTest(TestCase):
    def test_demo(self):
        self.assertEqual(1 + 1, 2)
