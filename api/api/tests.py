from django.test import TestCase

from api.calc import add

class CalcTests(TestCase):
# test function start always with test word    
    def test_add_numbers(self):
        """Test that two number are added toghether"""
        self.assertEqual(add(7, 3), 10)