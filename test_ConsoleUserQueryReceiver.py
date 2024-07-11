# Standard
import unittest
from unittest.mock import patch
import io

# Local
import UserQueryReceiver


class Test_ConsoleUserQueryReceiver(unittest.TestCase):
    
    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdin', io.StringIO('Typed text response'))
    def test_GetRawResponse(self):
        exp_val = 'Typed text response'
        act_val = UserQueryReceiver.UserQueryReceiver_GetRawResponse('Please type a text response and hit enter.')
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_IssueErrorMessage(self, mock_stdout):
        exp_val = 'Some printed error message\n'
        act_val = UserQueryReceiver.UserQueryReceiver_IssueErrorMessage('Some printed error message')
        self.assertEqual(exp_val, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
