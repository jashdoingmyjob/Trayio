import unittest
from trayio_roomba import clean_up


class TestCleanUpFunc(unittest.TestCase):

    def test_example_inputs(self):
        self.assertEqual(clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW")['final hoover position'], '1 3')
        self.assertEqual(clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW")['patches of dirt cleaned'], 1)

    def test_negative_x_dim(self):
        self.assertEqual(clean_up([-5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW"), {"Invalid dimensions. Dimensions must be positive": [-5, 5]})

    def test_negative_y_dim(self):
        self.assertEqual(clean_up([5, -5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW"), {"Invalid dimensions. Dimensions must be positive": [5, -5]})


if __name__ == '__main__':
    unittest.main()
