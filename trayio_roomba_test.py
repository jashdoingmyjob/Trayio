import unittest
from trayio_roomba import clean_up, extract_parameters_from_file


class TestCleanUpFunc(unittest.TestCase):

    def test_example_inputs(self):
        self.assertEqual(clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW")['final hoover position'], '1 3')
        self.assertEqual(clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW")['patches of dirt cleaned'], 1)


class TestExtractFunc(unittest.TestCase):
    def test_negative_x_dim(self):
        self.assertRaises(Exception, lambda: extract_parameters_from_file())
    def test_negative_y_dim(self):
        self.assertRaises(Exception, lambda: extract_parameters_from_file())


if __name__ == '__main__':
    unittest.main()
