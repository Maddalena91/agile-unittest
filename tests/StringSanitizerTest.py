import unittest
import sys
import os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)]) 
from StringSanitizer import StringSanitizer

class StringSanitizerTest(unittest.TestCase):
    def test_replace(self):
        sanitize = StringSanitizer()
        SanitizerString = sanitize.sanitize("a_string_to_be_sanitized")
        print(SanitizerString)
        self.assertEqual(SanitizerString, "a string to be sanitized")

if __name__ == '__main__':
    unittest.main()