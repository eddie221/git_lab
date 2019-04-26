#import python的unittest
import unittest
import Calculate as calculate

class Test(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(calculate.add(10, 3), 13)

    def test_add2(self):
        self.assertEqual(calculate.add(1, 4), 5)

    def test_add3(self):
        self.assertEqual(calculate.add(4, 4.7), 8.7)

    def test_minus1(self):
        self.assertEqual(calculate.minus(4, 1), 3)

    def test_minus2(self):
        self.assertEqual(calculate.minus(8, 4), 4)

    def test_minus3(self):
        self.assertEqual(calculate.minus(9.7, 2.5), 7.2)

    def test_mult1(self):
        self.assertEqual(calculate.mult(2, 3), 6)

    def test_mult2(self):
        self.assertEqual(calculate.mult(2, 39), 78)

    def test_mult3(self):
        self.assertEqual(calculate.mult(3.5, 2.1), 7.35)

    def test_div1(self):
        self.assertEqual(calculate.div(9, 3), 3)

    def test_div2(self):
        self.assertEqual(calculate.div(9, 0), "nan")

    def test_div3(self):
        self.assertEqual(calculate.div(5.4, 3), 1.8)

if __name__ == '__main__':
    unittest.main()