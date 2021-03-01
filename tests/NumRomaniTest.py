import unittest
import sys
import os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)]) 
from NumRomani import NumRomani

class NumRomaniTest(unittest.TestCase):
    def testIstance(self):
        r = NumRomani("v")
        self.assertIsInstance(r,NumRomani)

    def testSum(self):
        r = NumRomani("MCMXLIV")
        self.assertEqual(1944,r.ToInteger())
    
    def testSubtraction(self):
        r = NumRomani("XL")
        self.assertEqual(40,r.ToInteger())

    def testErrorNotisNumRoman(self):
        with self.assertRaisesRegex(Exception, "Sorry, il dato inserito non è un numero romano"):
            r = NumRomani("xp")

if __name__ == '__main__':
    unittest.main()