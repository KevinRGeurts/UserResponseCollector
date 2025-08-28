"""
This module provides a simple console application for testing the UserQueryReceiver and UserQueryCommand components.
The code in this module illustrates how to use these components to interactively query the user for different types of input.

__main__ executes a loop that asks the user to choose different query types to perform,
demonstrating the functionality of the UserQueryReceiver and various UserQueryCommand implementations.

Exported Classes:
    None

Exported Exceptions:
    None
 
Exported Functions:
    do_MenuQuery -- Use UserQueryReceiver and UserQueryCommandMenu to make a Menu query.
    do_NumberIntegerQuery -- Use UserQueryReceiver and UserQueryCommandNumberInteger to make a NumberInteger query.
    do_PathSaveQuery -- Use UserQueryReceiver and UserQueryCommandPathSave to make a PathSave query.
    do_PathOpenQuery -- Use UserQueryReceiver and UserQueryCommandPathOpen to make a PathOpen query.
    do_Debug -- Change the code inside this function to facilitate debugging.
"""

# Standard

# Local
from UserQueryCommand import UserQueryCommandMenu, UserQueryCommandPathOpen, UserQueryCommandPathSave, UserQueryCommandNumberInteger
import UserQueryReceiver


def do_Debug():
    """
    Use UserQueryReceiver to debug.
    """
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    query_preface = 'Enter a valid file system path.'
    command = UserQueryCommandPathSave(receiver, query_preface)
        
    exp_val = 'None'
    test_path = command.Execute()
    act_val = str(test_path)

    return None

def do_MenuQuery():
    """
    Use UserQueryReceiver to make a Menu query.
    """
    # Build a query for the user to obtain their choice from a menu
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    print(f"Receiver ID: {id(receiver)}")
    query_preface = 'Which menu item do you choose?'
    query_dic = {'a':'Option A', 'b':'Option B', 'c':'Option C'}
    command = UserQueryCommandMenu(receiver, query_preface, query_dic)    

    response = command.Execute()

    print(f"You chose {query_dic[response]} from the menu.")
    
    return None

def do_NumberIntegerQuery():
    """
    Use UserQueryReceiver to make a NumberInteger query.
    """
    # Build a query for the user to obtain an integer
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    print(f"Receiver ID: {id(receiver)}")
    query_preface = 'Which integer number do you want?'
    command = UserQueryCommandNumberInteger(receiver, query_preface, maximum = 1000)    

    response = command.Execute()

    print(f"You entered the integer {response}.")
    
    return None

def do_PathSaveQuery():
    """
    Use UserQueryReceiver to make a PathSave query.
    """
    # Build a query for the user to obtain a file save path
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    query_preface = 'To what file do you want to save?'
    command = UserQueryCommandPathSave(receiver, query_preface)
    
    test_path = command.Execute()
    
    print(f"You entered this path: {str(test_path)}")

    return None

def do_PathOpenQuery():
    """
    User UserQueryReceiver to make a PathOpen query.
    """
    # Build a query for the user to obtain a file open path
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    query_preface = 'Which file do you want to open?'
    command = UserQueryCommandPathOpen(receiver, query_preface)
    
    test_path = command.Execute()
    
    print(f"You entered this path: {str(test_path)}")

    return None

if __name__ == '__main__':
    
    """
    Query the user for how they wish to use UserQueryReceiver.
    """
    
    print('-------------------------------------------')
    print('*** UserQueryReceiver Testing Workbench ***')
    print('-------------------------------------------')
        
    # Build a query for the user to obtain their choice of how to user the workbench
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    print(f"Receiver ID: {id(receiver)}")
    query_preface = 'How do you want to use the workbench?'
    query_dic = {'q':'Quit', 'i':'Integer Query', 'm':'Menu Query', 'o':'File Open', 's':'File Save', 'd':'Debug'}
    command = UserQueryCommandMenu(receiver, query_preface, query_dic)    

    response = command.Execute() 
    
    while response != 'q':
        
        match response:
            
            case 'd':
                do_Debug()

            case 'i':
                do_NumberIntegerQuery()
                
            case 'm':
                do_MenuQuery()

            case 'o':
                do_PathOpenQuery()

            case 's':
                do_PathSaveQuery()
        
        print('--------------------')
        response = command.Execute() 

