# pylint
# auto Pep 8
# => unittest

import unittest
import main
from os import chdir

chdir('D:\\python\\python-dev-2020\\15-testing-in-python\\')

class TestMain(unittest.TestCase):
    # Runs setup code before each test
    def setUp(self):
        print('about to test function')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sadfas'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    # Runs tearDown code to reset variables etc after every test
    def tearDown(self):
        print('cleaning up variables')

class TestGame(unittest.TestCase):
    def test_input(self):
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

# To run unittests run | python -m unittest -v