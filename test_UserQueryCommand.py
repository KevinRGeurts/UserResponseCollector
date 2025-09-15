"""
This module provides unit tests for:
    (1) UserQueryCommand and (2) UserQueryCommandX classes
"""

# Standard
import unittest
from unittest.mock import patch
import io
import tempfile

# Local
from UserQueryCommand import UserQueryCommandMenu, UserQueryCommandNumberInteger, UserQueryCommandPathOpen, UserQueryCommandPathSave
from UserQueryCommand import UserQueryCommandNumberFloat, UserQueryCommandStr
from UserQueryCommand import askForMenuSelection, askForInt, askForFloat, askForStr, askForPathSave, askForPathOpen
import UserQueryReceiver

class Test_UserQueryCommandPathSaveOpen(unittest.TestCase):

    def test_PathSave_command_exists_y(self):
        
        # Create a named temporary file.
        temp_file = tempfile.NamedTemporaryFile()
        temp_path = temp_file.name
        print(f"temporary file path is: {temp_path}")
        # Use that named temporary file to patch sys.stadin
        patcher = patch('sys.stdin', io.StringIO(temp_path+'\ny\n'))
        # Start the patch
        patcher.start()
        # Make sure the patch gets undone during teardown
        self.addCleanup(patcher.stop)
        # Make sure the temporary file gets closed during teardown
        self.addCleanup(temp_file.close)
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Which file do you wish to save?'
        command = UserQueryCommandPathSave(receiver, query_preface)
        
        exp_val = temp_path
        test_path = command.Execute()
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)

    def test_PathSave_command_exists_n(self):

        # Create a named temporary file.
        temp_file = tempfile.NamedTemporaryFile()
        temp_path = temp_file.name
        print(f"temporary file path is: {temp_path}")
        # Use that named temporary file to patch sys.stadin
        patcher = patch('sys.stdin', io.StringIO(temp_path+'\nn\n'))
        # Start the patch
        patcher.start()
        # Make sure the patch gets undone during teardown
        self.addCleanup(patcher.stop)
        # Make sure the temporary file gets closed during teardown
        self.addCleanup(temp_file.close)        
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Which file do you wish to save?'
        command = UserQueryCommandPathSave(receiver, query_preface)
        
        exp_val = 'None'
        test_path = command.Execute()
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)

    def test_PathSave_function(self):

        # Create a named temporary file.
        temp_file = tempfile.NamedTemporaryFile()
        temp_path = temp_file.name
        print(f"temporary file path is: {temp_path}")
        # Use that named temporary file to patch sys.stadin
        patcher = patch('sys.stdin', io.StringIO(temp_path+'\nn\n'))
        # Start the patch
        patcher.start()
        # Make sure the patch gets undone during teardown
        self.addCleanup(patcher.stop)
        # Make sure the temporary file gets closed during teardown
        self.addCleanup(temp_file.close)        
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Which file do you wish to save?'
        exp_val = 'None'
        test_path = askForPathSave(query_preface)
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)

    def test_PathOpen_command(self):

        # Create a named temporary file.
        temp_file = tempfile.NamedTemporaryFile()
        temp_path = temp_file.name
        print(f"temporary file path is: {temp_path}")
        # Use that named temporary file to patch sys.stadin
        patcher = patch('sys.stdin', io.StringIO(temp_path+'\n'))
        # Start the patch
        patcher.start()
        # Make sure the patch gets undone during teardown
        self.addCleanup(patcher.stop)
        # Make sure the temporary file gets closed during teardown
        self.addCleanup(temp_file.close)
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Which file would you like to open?'
        command = UserQueryCommandPathOpen(receiver, query_preface)
        
        exp_val = temp_path
        test_path = command.Execute()
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)

    def test_PathOpen_function(self):

        # Create a named temporary file.
        temp_file = tempfile.NamedTemporaryFile()
        temp_path = temp_file.name
        print(f"temporary file path is: {temp_path}")
        # Use that named temporary file to patch sys.stadin
        patcher = patch('sys.stdin', io.StringIO(temp_path+'\nn\n'))
        # Start the patch
        patcher.start()
        # Make sure the patch gets undone during teardown
        self.addCleanup(patcher.stop)
        # Make sure the temporary file gets closed during teardown
        self.addCleanup(temp_file.close)        
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Which file would you like to open?'
        exp_val = temp_path
        test_path = askForPathOpen(query_preface)
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)


class Test_UserQueryCommand(unittest.TestCase):

    def test_bad_receiver_type(self):
        
        bad_receiver = '' # Note that it is a string, not a UserQueryReceiver
        self.assertRaises(AssertionError, UserQueryCommandMenu, bad_receiver, '', {})
    
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('0\n1\n'))
    def test_menu_command(self):
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Do you want option 1 or option 2?'
        query_dic = {'1':'Option 1', '2':'Option 2'}
        command = UserQueryCommandMenu(receiver, query_preface, query_dic)
        
        exp_val = '1'
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('0\n1\n'))
    def test_menu_function(self):
        query_preface = 'Do you want option 1 or option 2?'
        query_dic = {'1':'Option 1', '2':'Option 2'}
        exp_val = '1'
        act_val = askForMenuSelection(query_preface, query_dic)
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n10\n'))
    def test_NumberInteger_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'How many widgets do you want?'
        command = UserQueryCommandNumberInteger(receiver, query_preface)
        
        exp_val = 10
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n10\n'))
    def test_int_function(self):
        query_preface = 'How many widgets do you want?'
        exp_val = 10
        act_val = askForInt(query_preface)
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, then a response less than minimum, then a response greater than
    # maximum, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n0\n21\n10\n'))
    def test_NumberInteger_invalid_OutOfRange_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'How many widgets do you want?'
        command = UserQueryCommandNumberInteger(receiver, query_preface, minimum=1, maximum=20)
        
        exp_val = 10
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, then a response less than minimum, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n0\n10\n'))
    def test_NumberInteger_invalid_OutOfRange_noMax_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'How many widgets do you want?'
        command = UserQueryCommandNumberInteger(receiver, query_preface, minimum=1)
        
        exp_val = 10
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, then a response greater than maximum, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n21\n10\n'))
    def test_NumberInteger_invalid_OutOfRange_noMin_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'How many widgets do you want?'
        command = UserQueryCommandNumberInteger(receiver, query_preface, maximum=10)
        
        exp_val = 10
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n10.5\n'))
    def test_NumberFLoat_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'What is the distance in miles?'
        command = UserQueryCommandNumberFloat(receiver, query_preface)
        
        exp_val = 10.5
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n10.5\n'))
    def test_float_function(self):
        query_preface = 'What is the distance in miles?'
        exp_val = 10.5
        act_val = askForFloat(query_preface)
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, then a response less than minimum, then a response greater than
    # maximum, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n1.1\n20.84\n10.5\n'))
    def test_NumberFloat_invalid_OutOfRange_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'What is the distance in miles?'
        command = UserQueryCommandNumberFloat(receiver, query_preface, minimum=1.25, maximum=20.75)
        
        exp_val = 10.5
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)
        
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, then a response less than minimum, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n1.1\n10.5\n'))
    def test_NumberFloat_invalid_OutOfRange_noMax_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'What is the distance in miles?'
        command = UserQueryCommandNumberFloat(receiver, query_preface, minimum=1.25)
        
        exp_val = 10.5
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, then a response greater than maximum, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n20.85\n10.5\n'))
    def test_NumberFloat_invalid_OutOfRange_noMin_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'What is the distance in miles?'
        command = UserQueryCommandNumberFloat(receiver, query_preface, maximum=20.75)
        
        exp_val = 10.5
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response that is too long, then a valid response.
    @patch('sys.stdin', io.StringIO('George Washington\nG. Washington\n'))
    def test_Str_command(self):
 
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'What is your name?'
        command = UserQueryCommandStr(receiver, query_preface, max_length=15)
        
        exp_val = 'G. Washington'
        act_val = command.Execute()
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('George Washington\nG. Washington\n'))
    def test_str_function(self):
        query_preface = 'What is your name?'
        exp_val = 'G. Washington'
        act_val = askForStr(query_preface, max_length=15)
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
