import unittest
import sys
import os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)]) 
from Logger import Logger


class LoggerTest(unittest.TestCase):
    def testGetLog(self):
        l = Logger()
        l.Log("Test message log")
        l.Log("Test2 message log")
        mylist = [
            "Test message log",
            "Test2 message log"
            ]
        self.assertEqual(mylist, l.GetLog())
    
    def testEmptyGetLog(self):
        l = Logger()
        l.Log("")
        l.Log("Test2 message log")
        l.Log(" ")
        
        mylist = [
            "Test2 message log"
        ]
        self.assertEqual(mylist, l.GetLog())
        

        

if __name__ == '__main__':
    unittest.main()