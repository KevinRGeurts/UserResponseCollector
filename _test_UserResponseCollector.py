# Standard
import unittest
from unittest.mock import patch
import io

# Local
from UserResponseCollector import *
# from hand import Hand


class Test_UserResponseCollector(unittest.TestCase):
    
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\nh\n'))
    def test_menu_query(self):
        
        query_preface = 'Player''s hand: 2S QH.  Dealer shows: 8C.'
        query_dic = {'h':'Hit', 's':'Stand'}
        
        exp_val = 'h'
        act_val = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
        self.assertEqual(exp_val, act_val)
        
    
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('a\n10\n'))
    def test_number_query(self):
        
        query_preface = 'How many games do you want to automatically play?'
        
        exp_val = 10
        act_val = UserResponseCollector_query_user(BlackJackQueryType.NUMBER, query_preface)
        self.assertEqual(exp_val, act_val)
        

    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdin', io.StringIO('AS KH QD JC 10H 2S\n'))
    def test_cards_query(self):
        
        query_preface = 'Enter player deal up to two cards.'
        
        exp_val = 'AS KH QD JC 10H 2S'
        # card_list = UserResponseCollector_query_user(BlackJackQueryType.CARDS, query_preface)
        # h = Hand()
        # h.add_cards(card_list)
        # act_val = str(h)
        self.assertEqual(exp_val, act_val)

   
    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdin', io.StringIO('C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt\n'))
    def test_path_save_query(self):
        
        query_preface = 'Enter a valid file system path.'
        
        exp_val = 'C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt'
        test_path = UserResponseCollector_query_user(BlackJackQueryType.PATH_SAVE, query_preface)
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)

    # Apply a patch() decorator to replace keyboard input from user with a string.
    @patch('sys.stdin', io.StringIO('C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt\n'))
    def test_path_open_query(self):
        
        query_preface = 'Enter a valid file system path.'
        
        exp_val = 'C:\\Users\\krgeu\\Documents\\Cribbage_Output\\path_query_text.txt'
        test_path = UserResponseCollector_query_user(BlackJackQueryType.PATH_OPEN, query_preface)
        act_val = str(test_path)
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
