import unittest
import calc

class TestCalc(unittest.TestCase):
    #test_nameoftest is mandatory, else it won't work
    def test_add(self):
        self.assertEqual(calc.addition(10,5),15)
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertRaises(ValueError,calc.divide,10,0)
    def test_module(self):
        self.assertEqual(calc.module(10,5),0)
    def test_intdivision(self):
        self.assertEqual(calc.intdivision(10,5),2)
        self.assertRaises(ValueError,calc.intdivision,10,0)
    def test_power(self):
        self.assertEqual(calc.power(10,2),100)
        
#this line of code let me run my module directly, if it wasn't there, I should run it through CMD
#using python -m unittest test_calc        
if __name__=='__main__':
    unittest.main()
