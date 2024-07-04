# Standard
from enum import Enum
from pathlib import Path

# Local
# from card import Card


class UserResponseCollectorError(Exception):
    """
    Base exception class for all custom exceptions specific to UserResponseCollector.
    """
    pass

class UserResponseCollectorTerminateQueryingThreadError(UserResponseCollectorError):
    """
    Custom exception to be raised if the UserResonseCollector wants the query requester to terminate.
    Arguments expected in **kwargs:
        none at this time    
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


# TODO: Refactor this to make it "generalized" and "extensible". For example, the base version should support MENU and NUMBER query types.
# And the CARDS query type should be an extension specific to BlackJackSimulator.

# TODO: Objectify the query types as a children of a parent BlackJackUserQuery class.
# An instance of one of the children would be passed to the UserResponseCollector.query_user() method.
# An instance would have members to (1) prepare the prompt text to show to the user; (2) validate the raw response from the user or generate
# an error message for the user; (3) convert the raw response text from the user into an expected response type
# The parent could have the query_preface member. A "menu" child would have the query_dic member.
# UserResponseCollector.query_user() would: (1) call method of BlackJackUserQuery instance to get prompt string;
# (2) Use the prompt string to obtain a raw response from the user;
# (3) Call method of BlackJackUserQuery instance to validate the raw response (sharing error message with user and repeating (2) as needed;
# (4) Call method of BlackJackUserQuery instance to convert raw response to processed respoinse;
# (5) Return processed respones to caller.
# Note: (3) and (4) might happen in reverse or simultaneously.

class BlackJackQueryType(Enum):
    """
    An enumeration of types of queries that might be asked of a user of blackjack simulator.
    """
    MENU = 1 # Expect a response that matches a key in a dictionary of form {'h':'Hit', 's':'Stand'}, where the value are the menu choices.
    NUMBER = 2 # Expect a response of type int
    CARDS = 3 # Expect a response of a list of Card objects
    PATH_SAVE = 4 # Expect a response that is a valid Path object
    PATH_OPEN = 5 # Expect a response that is a valid Path object


class UserResponseCollector(object):
    """
    This class follows the Python Global Object Pattern, to provide a Singleton Pattern like object that can be used to obtain
    input from the user from stdin.
    References:
    (1) Global Object Pattern: https://python-patterns.guide/python/module-globals/
    (2) Prebound Method Pattern: https://python-patterns.guide/python/prebound-methods/
    """
    def __init__(self):
        """
        Just print a message, temporarily, to see if this works as expected and only ever gets instaniated once.
        """
        print('Instaniating: ', type(self))
        
    
    def query_user(self, query_type = BlackJackQueryType.MENU, query_preface = '', query_dic = {}):
        """
        Query the user (via terminal) and return the user's response, as the type expected.
        :parameter query_type: The type of request being made of the user, as BlackJackQueryType Enum
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter query_dic: Dictionary used when query_type = MENU. Values are string descriptions of the user's options.
            Keys are the value to return to the caller if the user selects each option.
        :return: The response of the user, type depends on query_type
        """
        processed_response = None
        
        match query_type:
            case BlackJackQueryType.MENU:
                processed_response =  self.process_menu_query(query_preface, query_dic)
            case BlackJackQueryType.NUMBER:
                processed_response = self.process_number_query(query_preface)
            case BlackJackQueryType.CARDS:
                processed_response = self.process_cards_query(query_preface)
            case BlackJackQueryType.PATH_SAVE:
                processed_response = self.process_path_save_query(query_preface)
            case BlackJackQueryType.PATH_OPEN:
                processed_response = self.process_path_open_query(query_preface)
        
        return processed_response


    def process_cards_query(self, query_preface = ''):
        """
        Query the user (via termainl) to enter a string that can be proccessed into a list of Cards, and return
        the list of Card objects.
        :parameter query_preface: Text displayed to the user to request their response, string
        :return: List of Card objects created from the user provided string
        """
        processed_response = None
        
        prompt_text = query_preface + '\n'

        # Add to the prompt, asking the user to enter a number.       
                
        prompt_text += '(examples AS KH QD JC 10S 9H 8D ... 2C): '
                
        while processed_response is None:
                
            # Ask the user for a response, which will be in the form of a string
            raw_response = input(prompt_text)
        
            # Process the response from the user into a list of Card objects
            try:
                # processed_response = Card().make_card_list_from_str(raw_response)
                pass
            except:
                # Let the user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid list of cards. Please try again.' 
                print(msg)
        
        return processed_response
    

    def process_number_query(self, query_preface = ''):
        """
        Query the user (via termainl) to enter a number, and return the user's response.
        :parameter query_preface: Text displayed to the user to request their response, string
        :return: The number entered by the user, int 
        """
        processed_response = None
        
        prompt_text = query_preface + '\n'

        # Add to the prompt, asking the user to enter a number.       
                
        prompt_text += 'Enter a number:  '
                
        while processed_response is None:
                
            # Ask the user for a response, which will be in the form of a string
            raw_response = input(prompt_text)
        
            # Process the response from the user into an integer
            try: 
                processed_response = int(raw_response)
            except:
                # Let the user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a number. Please try again.'
                print(msg)
        
        return processed_response
    
    def process_menu_query(self, query_preface = '', query_dic = {}):
        """
        Query the user (via terminal) to make a menu choice, and return the user's response.
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter query_dic: Values are string descriptions of the user's options. Keys are the value to return to
            the caller if the user selects each option.
        :return: The key of the menu option selected by the user, string 
        """       
        processed_response = None
        
        prompt_text = query_preface + '\n'

        # Add to the prompt the menu options available to the user       
                
        prompt_text += 'Choose '
                
        for (key, value) in query_dic.items():
            prompt_text += '(' + str(key) + ')' + str(value) + ', '
        # Remove unneeded trailing ', '
        prompt_text = prompt_text[0:len(prompt_text)-2]
        prompt_text += ':  '
        
        while processed_response is None:
                
            # Ask the user for a response, which will be in the form of a string
            raw_response = input(prompt_text)
        
            # Process the response from the user into a proper return value based on the query type
            if raw_response in query_dic:
                # User's input matches a key in the menu dictionary, so that's what we want to return
                processed_response = raw_response
            else:
                # Let the user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid response. Please try again.' 
                print(msg)
        
        return processed_response

    def process_path_save_query(self, query_preface = ''):
        """
        Query the user (via termainl) to enter a string that can be proccessed into a file path.
        :parameter query_preface: Text displayed to the user to request their response, string
        :return: Valid file path, as Path object
        """
        processed_response = None
        
        prompt_text = query_preface + '\n'

        # Add to the prompt, telling the user how to handle directory separaters   
                
        prompt_text += 'Enter a valid file system path, without file extension, and with escaped backslashes.'
                
        while processed_response is None:
                
            # Ask the user for a response, which will be in the form of a string
            raw_response = input(prompt_text)
        
            # Test that the user has provided a valid path
            # TODO: If the user has provided the path to an existing file, confirm that they wish to overwrite it.
            try:
                processed_response = Path(raw_response)
            except OSError:
                # Let the user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid file path. Please try again.' 
                print(msg)
        
        return processed_response        

    def process_path_open_query(self, query_preface = ''):
        """
        Query the user (via termainl) to enter a string that can be proccessed into a file path.
        :parameter query_preface: Text displayed to the user to request their response, string
        :return: Valid file path, as Path object
        """
        processed_response = None
        
        prompt_text = query_preface + '\n'

        # Add to the prompt, telling the user how to handle directory separaters   
                
        prompt_text += 'Enter a valid file system path, without file extension, and with escaped backslashes.'
                
        while processed_response is None:
                
            # Ask the user for a response, which will be in the form of a string
            raw_response = input(prompt_text)
        
            # Test that the user has provided a valid path
            try:
                processed_response = Path(raw_response)
            except OSError:
                # Let the user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid file path. Please try again.' 
                print(msg)
        
        return processed_response        


# Here is the global (intended to be private), single instance
_instance = UserResponseCollector()

# Here is the global prebound method(s)
UserResponseCollector_query_user = _instance.query_user


    