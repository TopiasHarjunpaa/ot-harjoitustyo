import unittest
from classtest import classs

class Testclasss(unittest.TestCase):
    def setUp(self):
        self.test = classs("testing")
    
    def test_print(self):
        self.assertEqual(str(self.test), "testing")