import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(Utils.reversed(12345), 54321)
        with self.assertRaises(ValueError):
            Utils.reversed("12345")
        with self.assertRaises(ValueError):
            Utils.reversed(15.12)
    
    def test_formatter(self):
        self.assertEqual(Utils.formatter(12345), ('0b11000000111001', '0o30071'))
        with self.assertRaises(ValueError):
            Utils.reversed("12345")
        with self.assertRaises(ValueError):
            Utils.reversed(15.12)
            
if __name__ == "__main__":
    unittest.main()