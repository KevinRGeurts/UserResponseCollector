# Standard

# Local

class UserQueryCommand(object):
    """
    Following the Command design pattern, this is the abstract base or interface class for ConcreateUserQueryCommand classes that know how to execute
    various user querys by invoking prebound methods on UserQueryReceiver.
    Each child must by convention and necessity implement these methods:
        Execute(...) - Blah, blah
        Y(...) - Blah, blay
    """
    def __init__(self):
        """
        """
        
        pass
    
    def Execute(self):
        """
        This is an abstract method that MUST be implemented by children. If called, it will raise NotImplementedError
        Called to obtain a response from the user, of a type which can differ for each child
        :return: None        
        """
        raise NotImplementedError
        return None
    
    # Will probably also need methods for:
    # Processing and validation of raw response into processed response
    # Possibly to return the type of the processed response
    #
    #
 
class UserQueryCommandMenu(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a menu command.
    """
    def __init__(self, query_preface = '', query_dic = {}):
        """
        :parameter query_preface: Text displayed to the user to request their response, string
        :parameter query_dic: Values are string descriptions of the user's options. Keys are the value the Client/Invoker are requesting.
        """
        UserQueryCommand.__init__(self)
        self._query_preface = query_preface
        self._query_dic = query_dic
        
    def Execute(self):
        """
        Execution of Menu command returns the key of the value from query_dic that the user selected.
        :return: key from query_dic        
        """
        

        return None


