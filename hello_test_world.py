import unittest
from unittest.mock import patch
from unittest import TestCase


def get_input(text):
    return input(text)


def answer():
    ans = input('enter yes or no')
    if ans == 'yes':
        ans = input('enter yes or no')
        if ans == 'yes':
            ans = input('enter yes or no')
            return 'you entered yes'
        if ans == 'no':
            return 'you entered no'
    else:
        return 'Nope'
#        return 'you entered yes'
#    if ans == 'no':
#        return 'you entered no'

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3),4)

    # get_input will return 'yes' during this test
    @patch('builtins.input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('builtins.input', return_value='yes \n no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')


if __name__ == '__main__':
    unittest.main()
