# Standard
import unittest
from unittest.mock import patch
import io

# Local
from UserQueryCommand import UserQueryCommandMenu, UserQueryCommandNumberInteger, UserQueryCommandPathSave

class Test_UserQueryCommand(unittest.TestCase):
    
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('0\n1\n'))
    def test_menu_command(self):
        
        # TODO: receiver = ConsoleUserQueryReceiver() ??
        receiver = None
        query_preface = 'Do you want option 1 or option 2?'
        query_dic = {'1':'Option 1', '2':'Option 2'}
        command = UserQueryCommandMenu(receiver, query_preface, query_dic)
        
        exp_val = '1'
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n10\n'))
    def test_NumberInteger_command(self):
 
        # TODO: receiver = ConsoleUserQueryReceiver() ??
        receiver = None        
        query_preface = 'How many widgets do you want?'
        command = UserQueryCommandNumberInteger(receiver, query_preface)
        
        exp_val = 10
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)
    
    # TODO: Fix (generalize) the test path, which is a complete hack at this point
    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdin', io.StringIO('C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt\n'))
    def test_PathSave_command(self):
        
        # TODO: receiver = ConsoleUserQueryReceiver() ??
        receiver = None
        query_preface = 'Enter a valid file system path.'
        command = UserQueryCommandPathSave(receiver, query_preface)
        
        exp_val = 'C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt'
        test_path = command.Execute()
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)
        
    # TODO: Fix (generalize) the test path, which is a complete hack at this point
    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdin', io.StringIO('C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt\n'))
    def test_PathOpen_command(self):
        
        # TODO: receiver = ConsoleUserQueryReceiver() ??
        receiver = None
        query_preface = 'Enter a valid file system path.'
        command = UserQueryCommandPathSave(receiver, query_preface)
        
        exp_val = 'C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt'
        test_path = command.Execute()
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)
        

if __name__ == '__main__':
    unittest.main()
