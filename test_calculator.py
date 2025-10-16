import unittest
from calculator import add , subtract , multiply , divide

class TestCalculator(unittest.TestCase):
  def addTest(self):
    self.assertEqual(add(2,2),4)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(0, 0), 0)
    
  def test_subtract(self):
        """Test phép trừ"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 10), 0)
    
  def test_multiply(self):
        """Test phép nhân"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 100), 0)
    
  def test_divide(self):
        """Test phép chia"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
    
  def test_divide_by_zero(self):
        """Test chia cho 0"""
        with self.assertRaises(ValueError):
            divide(10, 0)
if __name__ == '__main__':
  unittest.main()
