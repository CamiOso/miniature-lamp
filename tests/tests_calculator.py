import unittest
from  src.calculator import suma,resta,multiplicacion,division

class CalculatorTests(unittest.TestCase):
    def test_suma(self):
        assert suma(2,3)==5

    def test_resta(self):
        assert resta(3,1)==2

    def test_multiplicacion(self):
        assert multiplicacion(2,3)==6

    def test_division(self):
        resultado=division(10,2)
        expected=5
        assert resultado==expected


    
