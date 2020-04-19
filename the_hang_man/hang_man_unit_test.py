#TODO: teste automatico de inputs pelo promt
import unittest
from unittest.mock import patch
from hang_man import *

class UnitTestClass(unittest.TestCase):
    def test(self):
        #play_hang_man()
        self.assertEqual(validate_input("test"), True)
        self.assertEqual(validate_input("two words"), False)
        self.assertEqual(validate_input("2"), False)
        self.assertEqual(check_letter("oi","o"), 0)
        self.assertEqual(check_letter("oi","a"), -1)
        self.assertEqual(iteration_result(-1,'a',[0,0,['_','_']]), [1,0, ['_','_']])
        self.assertEqual(iteration_result(1,'i',[0,0,['_','_']]), [0,1,['_','i']])
        @patch('builtins.input', return_value='oi \n o \n i')
        def test_guess_rigth(self, input):
            self.assertEqual(play_hang_man(), 'Got it!')
        @patch('builtins.input', return_value='oi \n a \n a')
        def test_guess_wrong(self, input):
            self.assertEqual(play_hang_man(), 'Too bad :T')

if __name__ == '__main__':
    unittest.main()
