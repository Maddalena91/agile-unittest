import unittest
import sys
import os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)]) 
from Money import Money

class MoneyTest(unittest.TestCase):
    def testCreate(self):
        num = Money(10)
        self.assertIsInstance(num,Money)
        self.assertEqual(10,num.getNumber())

    def testIsGreaterThan(self):
        object1 = Money(10)
        object2 = Money(5)
        self.assertTrue(object1.isGreaterThan(object2))
    
    def testIsLessThan(self):
        object1 = Money(5)
        object2 = Money(10)
        self.assertTrue(object1.isLessThan(object2))

    def testSum(self):
        object1 = Money(5)
        object2 = Money(10)
        n = object1.sum(object2)
        self.assertIsInstance(n,Money)
        self.assertEqual(15,n.getNumber())

    def testSubtraction(self):
        object1 = Money(10)
        object2 = Money(5)
        n = object1.subtraction(object2)
        self.assertIsInstance(n,Money)
        self.assertEqual(5,n.getNumber())

    def testErrorNumberNegative(self):
        with self.assertRaisesRegex(Exception, "Sorry, il numero è negativo"):
            object1 = Money(5)
            object2 = Money(10)
            n = object1.subtraction(object2)
        with self.assertRaisesRegex(Exception, "Sorry, il numero inserito non può essere negativo"):
            num = Money(-10)

    def testErrorNumberInt(self):
        with self.assertRaisesRegex(TypeError, "Sorry, il numero non è un intero"):
            num = Money(10.0)
            
    def testErrorNumberString(self):
        with self.assertRaisesRegex(Exception, "Sorry, le stringhe non sono accettate"):
            num = Money("-10")
    

if __name__ == '__main__':
    unittest.main()