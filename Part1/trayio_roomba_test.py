import unittest
from trayio_roomba import Roomba


class TestCleanUpFunc(unittest.TestCase):

    def test_example_inputs(self):
        r = Roomba()
        self.assertEqual(r.clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW")['final hoover position'], '1 3')
        self.assertEqual(r.clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNESEESWNWW")['patches of dirt cleaned'], 1)

    def test_bad_instruction(self):
        r = Roomba()
        self.assertEqual(r.clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNZESEESWNWW")['final hoover position'], '1 3')
        self.assertEqual(r.clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "NNZESEESWNWW")['patches of dirt cleaned'], 1)

    def test_lowercase_inputs(self):
        r = Roomba()
        self.assertEqual(r.clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "nnESeESwNWW")['final hoover position'], '1 3')
        self.assertEqual(r.clean_up([5, 5], [1, 2], [(1, 0), (2, 2), (2, 3)], "nnESeESwNWW")['patches of dirt cleaned'], 1)

    def test_new_inputs(self):
        r = Roomba()
        self.assertEqual(r.clean_up([16, 11], [2, 2], [(2, 3), (3, 6), (3, 7), (5, 4)], "NENNNNEESSS")['final hoover position'], '5 4')
        self.assertEqual(r.clean_up([16, 11], [2, 2], [(2, 3), (3, 6), (3, 7), (5, 4)], "NENNNNEESSS")['patches of dirt cleaned'], 4)

    def test_negative_dirt_loc_inputs(self):
        r = Roomba()
        self.assertEqual(r.clean_up([16, 11], [2, 2], [(-2, 3), (3, -6), (3, 7), (5, 4)], "NENNNNEESSS")['final hoover position'], '5 4')
        self.assertEqual(r.clean_up([16, 11], [2, 2], [(-2, 3), (3, -6), (3, 7), (5, 4)], "NENNNNEESSS")['patches of dirt cleaned'], 2)

    def test_wall_hitting_instructions(self):
        r = Roomba()
        self.assertEqual(r.clean_up([16, 11], [2, 2], [(2, 3), (3, 6), (3, 7), (5, 4)], "SSSNNNENNNNEESSS")['final hoover position'], '5 4')
        self.assertEqual(r.clean_up([16, 11], [2, 2], [(2, 3), (3, 6), (3, 7), (5, 4)], "SSSNNNENNNNEESSS")['patches of dirt cleaned'], 4)


class TestExtractFunc(unittest.TestCase):
    def test_negative_x_dim(self):
        r = Roomba()
        self.assertRaises(ValueError, r.extract_parameters_from_file, 'test_input1.txt')

    def test_negative_y_dim(self):
        r = Roomba()
        self.assertRaises(ValueError, r.extract_parameters_from_file, 'test_input2.txt')


if __name__ == '__main__':
    unittest.main()
