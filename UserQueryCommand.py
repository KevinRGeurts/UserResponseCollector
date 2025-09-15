"""
Defines the interface and concrete implementations of UserQueryCommands classes that know how to query the
user for different types of input (e.g., menu choice, integer number, file path) via a UserQueryReceiver concrete
implementation.

Following the Command design pattern, the Command participant interface is defined, and and multiple ConcreteCommand
implementations are provided.

Exported Classes:
    UserQueryCommand -- Interface (abstract base) class for Command.
    UserQueryCommandX -- Concrete UserQueryCommand that invokes methods on UserQueryReceiver to obtain user input of type X.
    
Exported Exceptions:
    None    
 
Exported Functions:
    askForMenuSelection(...) -- Convenience function to query user to select a menu option without using objects.
    askForInt(...) -- Convenience function to query user for an integer number without using objects.
    askForFloat(...) -- Convenience function to query user for a floating point number without using objects.
    askForStr(...) -- Convenience function to query user for a text string without using objects.
    askForPathSave(...) -- Convenience function to query user for a path to save a file without using objects.
    askForPathOpen(...) -- Convenience function to query user for a path to open a file without using objects.
"""

# Standard
from pathlib import Path

# Local
import UserQueryReceiver

class UserQueryCommand(object):
    """
    Following the Command design pattern, this is the abstract base or interface class for ConcreateUserQueryCommand classes that know how to execute
    various user querys by invoking methods on UserQueryReceiver.

    Each child must by convention and necessity implement these methods:
        Execute(...) - Called to obtain a response from the user, of a type which can differ for each child.
    """
    def __init__(self, receiver=None):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command, must be a UserQueryReceiver instance.
        """
        assert(isinstance(receiver, UserQueryReceiver.UserQueryReceiver))
        self._receiver = receiver
    
    def Execute(self):
        """
        This is an abstract method that MUST be implemented by children. If called, it will raise NotImplementedError
        Called to obtain a response from the user, of a type which can differ for each child.
        :return: None        
        """
        raise NotImplementedError
        return None

 
class UserQueryCommandMenu(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreteUserQueryCommand class that knows how to exeucte a menu command.
    Query the user via receiver to select from a menu of options.

    Methods:
        Execute(...) --- Returns the key of the value from the query dictionary that the user selected.
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
        Execution of Menu command returns the key of the value from query_dic that the user selected. User will be prompted with text:
            {query_preface passed in constructor}
            Choose (key1)value1, (key2)value2, ... :        
        
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
        
            # Process the raw response from the receiver/user into a proper return value for this query type
            if raw_response in self._query_dic:
                # User's input matches a key in the menu dictionary, so that's what we want to return
                processed_response = raw_response
            else:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid response. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
 
        return processed_response


# Convenience function to query user to select a menu option without using objects.
def askForMenuSelection(query_preface = '', query_dic = {}):
    """
    This is a convenience fuction to query user to select a menu option without using objects.
    Returns the key of the value from query_dic that the user selected. User will be prompted with text:
        {query_preface argument}
        Choose (key1)value1, (key2)value2, ... :        

    :parameter query_preface: Text displayed to the user to request their response, string
    :parameter query_dic: Values are string descriptions of the user's options. Keys are the value the Client/Invoker are requesting.
        
    :return: key from query_dic   
    """
    # Build a query for the user to obtain their choice from a menu
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    command = UserQueryCommandMenu(receiver, query_preface, query_dic)    
    response = command.Execute()
    return response


class UserQueryCommandNumberInteger(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a NumberInteger command.
    Query the user via receiver to provide an integer number within a specified range.

    Methods:
        Execute(...) --- Returns the integer value provided by the user.
    """
    def __init__(self, receiver=None, query_preface = '', minimum=None, maximum=None):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter minimum: The minimum valid entered integer response, int
            If None, then there is no minimum value.
        :parameter maximum: The maximum valid entered ingeger response, int
            If None, then there is no maximum value.
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        self._min_val = minimum
        self._max_val = maximum
        
    def Execute(self):
        """
        Execution of NumberInteger command returns the integer value provided by the user. User will be prompted with text:
            {query_preface passed in constructor}
            Enter an integer number between {minimum passed in constructor} and {maximum passed in constructor}:
        
        :return: The integer number entered by the user, int        
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, asking the user to enter a number.       
                
        prompt_text += f"Enter an integer number between {self._min_val} and {self._max_val}:  "
        
        while processed_response is None:
                
            # Ask the receiver/user for a raw response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Process the response from the receiver/user into an integer
            try: 
                processed_response = int(raw_response)
                # Check if the entered integer is within range, if the user has provided min and max values
                if self._min_val:
                    if processed_response < self._min_val:
                        # Let the receiver/user know they provided an invalid response
                        msg = f"\n\'{raw_response}\' is less than {self._min_val}. Please try again."
                        self._receiver.IssueErrorMessage(msg)
                        processed_response = None # So that we go around the while again
                        continue
                if self._max_val:
                    if processed_response > self._max_val:
                        # Let the receiver/user know they provided an invalid response
                        msg = f"\n\'{raw_response}\' is greater than {self._max_val}. Please try again."
                        self._receiver.IssueErrorMessage(msg)
                        processed_response = None # So that we go around the while again
            except:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not an integer. Please try again.'
                self._receiver.IssueErrorMessage(msg)
                
        return processed_response


# Convenience function to query user for an integer number without using objects.
def askForInt(query_preface = '', minimum=None, maximum=None):
    """
    This is a convenience fuction to query user for an integer number without using objects.
    Returns the valid integer number that the user entered. User will be prompted with text:
        {query_preface argument}
        Enter an integer number between {minimum argument} and {maximum argument}:       

    :parameter query_preface: Text displayed to the user to request their response, string
    :parameter minimum: The minimum valid entered integer response, int
        If None, then there is no minimum value.
    :parameter maximum: The maximum valid entered ingeger response, int
        If None, then there is no maximum value.
        
    :return: The integer number entered by the user, int    
    """
    # Build a query for the user to obtain an integer value
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    command = UserQueryCommandNumberInteger(receiver, query_preface, minimum, maximum)    
    response = command.Execute()
    return response
    

class UserQueryCommandNumberFloat(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a NumberFloat command.
    Query the user via receiver to provide an floating point number within a specified range.

    Methods:
        Execute(...) --- Returns the floating point value provided by the user.
    """
    def __init__(self, receiver=None, query_preface = '', minimum=None, maximum=None):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter minimum: The minimum valid entered floating point number response, float
            If None, then there is no minimum value.
        :parameter maximum: The maximum valid entered floating point number response, float
            If None, then there is no maximum value.
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        self._min_val = minimum
        self._max_val = maximum
        
    def Execute(self):
        """
        Execution of NumberFloat command returns the floating point value provided by the user. User will be prompted with text:
            {query_preface passed in constructor}
            Enter a floating point number between {minimum passed in constructor} and {maximum passed in constructor}:
        
        :return: The floating point number entered by the user, float        
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, asking the user to enter a number.       
                
        prompt_text += f"Enter a floating point number between {self._min_val} and {self._max_val}:  "
        
        while processed_response is None:
                
            # Ask the receiver/user for a raw response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Process the response from the receiver/user into an integer
            try: 
                processed_response = float(raw_response)
                # Check if the entered floating point value is within range, if the user has provided min and max values
                if self._min_val:
                    if processed_response < self._min_val:
                        # Let the receiver/user know they provided an invalid response
                        msg = f"\n\'{raw_response}\' is less than {self._min_val}. Please try again."
                        self._receiver.IssueErrorMessage(msg)
                        processed_response = None # So that we go around the while again
                        continue
                if self._max_val:
                    if processed_response > self._max_val:
                        # Let the receiver/user know they provided an invalid response
                        msg = f"\n\'{raw_response}\' is greater than {self._max_val}. Please try again."
                        self._receiver.IssueErrorMessage(msg)
                        processed_response = None # So that we go around the while again
            except:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a floating point. Please try again.'
                self._receiver.IssueErrorMessage(msg)
                
        return processed_response


# Convenience function to query user for a floating point value without using objects.
def askForFloat(query_preface = '', minimum=None, maximum=None):
    """
    This is a convenience fuction to query user for a floating point value without using objects.
    Returns the valid floating point number that the user entered. User will be prompted with text:
        {query_preface argument}
        Enter a floating point number between {minimum argument} and {maximum argument}:       

    :parameter query_preface: Text displayed to the user to request their response, string
    :parameter minimum: The minimum valid entered floating point response, float
        If None, then there is no minimum value.
    :parameter maximum: The maximum valid entered floating point response, float
        If None, then there is no maximum value.
        
    :return: The floating point number entered by the user, float    
    """
    # Build a query for the user to obtain a floating point value
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    command = UserQueryCommandNumberFloat(receiver, query_preface, minimum, maximum)    
    response = command.Execute()
    return response


class UserQueryCommandStr(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a Str command.
    Query the user via receiver to provide a string.

    Methods:
        Execute(...) --- Returns the valid string provided by the user.
    """
    def __init__(self, receiver=None, query_preface = '', max_length = 25):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter max_length: The maximum valid entered string length, int
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        self._max_len = max_length
        
    def Execute(self):
        """
        Execution of Str command returns the string of valid length provided by the user. User will be prompted with text:
            {query_preface passed in constructor}
            Enter a string of text no longer than {maximum length passed in constructor} characters.
        
        :return: String of text entered by user, as string
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt  
                
        prompt_text += f"Enter a string of text no longer than {self._max_len} characters."
                
        while processed_response is None:
                
            # Ask the reciever/user for a response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Test that the receiver/user has provided a valid path using try/except
            try:
                processed_response = str(raw_response)
                # Check if the entered string is within the maximum length
                if self._max_len:
                    if len(processed_response) > self._max_len:
                        # Let the receiver/user know they provided an invalid response
                        msg = f"\n\'{raw_response}\' is longer than {self._max_len} characters. Please try again."
                        self._receiver.IssueErrorMessage(msg)
                        processed_response = None # So that we go around the while again
            except:
                # Let the receiver/user know they provided an invalid response, which probably isn't possible
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid string of text. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
        
        return processed_response


# Convenience function to query user for a text string without using objects.
def askForStr(query_preface = '', max_length=25):
    """
    This is a convenience fuction to query user for a text string without using objects.
    Returns the valid length text string that the user entered. User will be prompted with text:
        {query_preface argument}
        Enter a string of text no longer than {max_length argument} characters.      

    :parameter query_preface: Text displayed to the user to request their response, string
    :parameter max_length: The maximum valid entered string length, int
        If None, then there is no maximum length. Default is 25.
        
    :return: The text string entered by the user, str    
    """
    # Build a query for the user to obtain a text string
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    command = UserQueryCommandStr(receiver, query_preface, max_length=max_length)    
    response = command.Execute()
    return response


class UserQueryCommandPathSave(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a PathSave command.
    Query the user via receiver to provide a file path.

    Methods:
        Execute(...) --- Returns the valid file path provided by the user.
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
        Execution of PathSave command returns the valid file path provided by the user. User will be prompted with text:
            {query_preface passed in constructor}
            Enter a valid file system path, without file extension, and with escaped backslashes.
        
        If the path provided already exists, the user will be asked to confirm they want to overwrite it. If not,
        then they will be prompted to enter a new path.

        :return: Valid file path, as Path object
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, telling the user how to handle directory separaters   
                
        prompt_text += 'Enter a valid file system path, without file extension, and with escaped backslashes.'
                
        while processed_response is None:
                
            # Ask the reciever/user for a response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Test that the receiver/user has provided a valid path using try/except
            try:
                processed_response = Path(raw_response)
                # Check if the receiver / user has provided the path to an existing file. If so, confirm that the wish to overwrite it.
                if processed_response.exists():
                    query_preface = '\n' + '\'' + raw_response + '\'' + ' is an existing file. Do you want to overwrite it?'
                    query_dic = {'y':'Yes', 'n':'No'}
                    command = UserQueryCommandMenu(self._receiver, query_preface, query_dic)
                    overwrite_response = command.Execute()
                    match overwrite_response:
                        case 'n':
                            processed_response = None
                            break
            except OSError:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid file path. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
        
        return processed_response

 
# Convenience function to query user for a path to save a file without using objects.
def askForPathSave(query_preface = ''):
    """
    This is a convenience fuction to query user for a path to save a file without using objects.
    Returns the valid file path that the user entered. User will be prompted with text:
        {query_preface argument}
        Enter a valid file system path, without file extension, and with escaped backslashes.      

    If the path provided already exists, the user will be asked to confirm they want to overwrite it. If not,
    then they will be prompted to enter a new path.

    :parameter query_preface: Text displayed to the user to request their response, string
        
    :return: Valid file path, as Path object   
    """
    # Build a query for the user to obtain a file save path
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    command = UserQueryCommandPathSave(receiver, query_preface)    
    response = command.Execute()
    return response    


class UserQueryCommandPathOpen(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a PathOpen command.
    Query the user via receiver to provide a file path.

    Methods:
        Execute(...) --- Returns the valid file path provided by the user.
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
        Execution of PathSave command returns the valid file path provided by the user. User will be prompted with text:
            {query_preface passed in constructor}
            Enter a valid file system path, without file extension, and with escaped backslashes.
        
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

# Convenience function to query user for a path to open a file without using objects.
def askForPathOpen(query_preface = ''):
    """
    This is a convenience fuction to query user for a path to open a file without using objects.
    Returns the valid file path that the user entered. User will be prompted with text:
        {query_preface argument}
        Enter a valid file system path, without file extension, and with escaped backslashes.      

    :parameter query_preface: Text displayed to the user to request their response, string
        
    :return: Valid file path, as Path object   
    """
    # Build a query for the user to obtain a file open path
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    command = UserQueryCommandPathOpen(receiver, query_preface)    
    response = command.Execute()
    return response   