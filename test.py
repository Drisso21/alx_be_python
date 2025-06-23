import unittest

import unittest

def square(x):
    return x*2
class TestSquareFunction(unittest.TestCase):
    def test_square_pos(self):
        self.assertEqual(square(2), 4)
    def test_square_neg(self):
        self.assertEqual(square(-3), 9)
    def test_square_zero(self):
        self.assertEqual(square(0), 0)
if __name__ == "__main__":
  unittest.main()