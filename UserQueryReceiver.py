# Standard

# Local


class UserQueryReceiver(object):
    """
    Following the Command design pattern, this is the abstract base or interface class for Receiver classes that know how to perform operations
    required to carry out a concrete UserQueryCommand. We will also be applying the Global Object and Prebound Method patterns.
    Each child must by convention and necessity implement these methods:
        GetRawResponse(...) - Obtains from the user their actual raw response as a string of text, for example, typed into a console window 
        IssueErrorMessage(...) - Informs the user that their raw response does not meet requirements.
    """
    def __init__(self):
        """
        Just print a message, temporarily, to see if this works as expected and only ever gets instaniated once.
        """
        print(f"Instaniating: {type(self)}, ID: {id(self)}")
            
    def GetCommandReceiver(self):
        """
        This is a concreate method, intended to be used as the target of a prebound method. It returns self.
        :return: self, UserQueryReceiver object       
        """
        return self
    
    def GetRawResponse(self, prompt_text=''):
        """
        This is an abstract method that MUST be implemented by children. If called, it will raise NotImplementedError
        Called to obtain a raw response from the user, which will always be a sting of text.
        :parameter prompt_text: String of text to use to tell the user what response is requrired, string
        :return: raw_response, string        
        """
        raw_response = ''
        raise NotImplementedError
        return raw_response
    
    def IssueErrorMessage(self, msg=''):
        """
        This is an abstract method that MUST be implemented by children. If called, it will raise NotImplementedError
        Called to inform the user that their raw response does not meet requirements.
        :parameter msg: Error message to be shown to the user, string
        :return: None       
        """
        raise NotImplementedError
        return None
    
    
class ConsoleUserQueryReceiver(UserQueryReceiver):
    """
    Following the Command design patUserQueryReceivertern, this is a concrete implementation of a UserQueryReceiver, that a concrete UserQueryCommand object
    can use to obtain raw responses from the user through a console window.
    """
    def __init__(self):
        """
        """
        UserQueryReceiver.__init__(self)
    
    def GetRawResponse(self, prompt_text=''):
        """
        Called to obtain a raw response from the user through thier interaction with a console window, which will always be a sting of text.
        :parameter prompt_text: String of text to use to tell the user what response is requrired, string
        :return: raw_response, string        
        """
        # Ask the user to type a text response into the console window, which will be in the form of a string
        raw_response = input(prompt_text)
        return raw_response
    
    def IssueErrorMessage(self, msg=''):
        """
        Called to inform the user that their raw response does not meet requirements.
        :parameter msg: Error message to be shown to the user, string
        :return: None       
        """
        # Let the user know that there was a problem with their response, by printing an error message to the console window
        print(msg)
        return None


# Here is the global (intended to be private), single instance
_instance = ConsoleUserQueryReceiver()

# Here are the global prebound method(s)
UserQueryReceiver_GetCommandReceiver = _instance.GetCommandReceiver
# UserQueryReceiver_GetRawResponse = _instance.GetRawResponse
# UserQueryReceiver_IssueErrorMessage = _instance.IssueErrorMessage

