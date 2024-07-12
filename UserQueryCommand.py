# Standard
from cmd import PROMPT
from pathlib import Path

# Local
import UserQueryReceiver

class UserQueryCommand(object):
    """
    Following the Command design pattern, this is the abstract base or interface class for ConcreateUserQueryCommand classes that know how to execute
    various user querys by invoking prebound methods on UserQueryReceiver.
    Each child must by convention and necessity implement these methods:
        Execute(...) - Blah, blah
        Y(...) - Blah, blay
    """
    def __init__(self, receiver=None):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        """
        assert(isinstance(receiver, UserQueryReceiver.UserQueryReceiver))
        self._receiver = receiver
    
    def Execute(self):
        """
        This is an abstract method that MUST be implemented by children. If called, it will raise NotImplementedError
        Called to obtain a response from the user, of a type which can differ for each child
        :return: None        
        """
        raise NotImplementedError
        return None

 
class UserQueryCommandMenu(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a menu command.
    """
    def __init__(self, receiver=None, query_preface = '', query_dic = {}):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter query_dic: Values are string descriptions of the user's options. Keys are the value the Client/Invoker are requesting.
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        self._query_dic = query_dic
        
    def Execute(self):
        """
        Execution of Menu command returns the key of the value from query_dic that the user selected.
        :return: key from query_dic        
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt the menu options available to the user       
                
        prompt_text += 'Choose '
                
        for (key, value) in self._query_dic.items():
            prompt_text += '(' + str(key) + ')' + str(value) + ', '
        # Remove unneeded trailing ', '
        prompt_text = prompt_text[0:len(prompt_text)-2]
        prompt_text += ':  '
        
        while processed_response is None:
                
            # Ask the receiver/user for a raw response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
            # For now, use the prebound object pattern
            # raw_response = UserQueryReceiver.UserQueryReceiver_GetRawResponse(prompt_text)
        
            # Process the raw response from the receiver/user into a proper return value for this query type
            if raw_response in self._query_dic:
                # User's input matches a key in the menu dictionary, so that's what we want to return
                processed_response = raw_response
            else:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid response. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
 
        return processed_response


class UserQueryCommandNumberInteger(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a NumberInteger command.
    """
    def __init__(self, receiver=None, query_preface = ''):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        
    def Execute(self):
        """
        Execution of NumberInteger command returns the integer value provided by the user.
        :return: The integer number entered by the user, int        
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, asking the user to enter a number.       
                
        prompt_text += 'Enter a number:  '
        
        while processed_response is None:
                
            # Ask the receiver/user for a raw response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Process the response from the receiver/user into an integer
            try: 
                processed_response = int(raw_response)
            except:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not an integer. Please try again.'
                self._receiver.IssueErrorMessage(msg)
                
        return processed_response
    

class UserQueryCommandPathSave(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a PathSave command.
    Query the user via receiver to provide a file path.
    """
    def __init__(self, receiver=None, query_preface = ''):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        
    def Execute(self):
        """
        Execution of PathSave command returns the valid file path provided by the user.
        :return: Valid file path, as Path object
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, telling the user how to handle directory separaters   
                
        prompt_text += 'Enter a valid file system path, without file extension, and with escaped backslashes.'
                
        while processed_response is None:
                
            # Ask the reciever/user for a response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Test that the receiver/user has provided a valid path
            # TODO: If the receiver/user has provided the path to an existing file, confirm that they wish to overwrite it.
            try:
                processed_response = Path(raw_response)
            except OSError:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid file path. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
        
        return processed_response

    
class UserQueryCommandPathOpen(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a PathOpen command.
    Query the user via receiver to provide a file path.
    """
    def __init__(self, receiver=None, query_preface = ''):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        
    def Execute(self):
        """
        Execution of PathSave command returns the valid file path provided by the user.
        :return: Valid file path, as Path object
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, telling the user how to handle directory separaters   
                
        prompt_text += 'Enter a valid file system path, without file extension, and with escaped backslashes.'
                
        while processed_response is None:
                
            # Ask the reciever/user for a response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Test that the receiver/user has provided a valid path
            try:
                processed_response = Path(raw_response)
            except OSError:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid file path. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
        
        return processed_response