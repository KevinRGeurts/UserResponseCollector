# Standard

# Local
from UserQueryCommand import UserQueryCommandMenu
import UserQueryReceiver


def do_X():
    """
    Use UserResponseCollector to do X.
    """

    return None

if __name__ == '__main__':
    
    """
    Query the user for how they wish to use UserResponseCollector.
    """
    
    print('--------------------')
    print('*** User Response Collector Testing Workbench ***')
    print('--------------------')
        
    # Build a query for the user to obtain their choice of how to user the workbench
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    print(f"Receiver ID: {id(receiver)}")
    query_preface = 'How do you want to use the workbench?'
    query_dic = {'q':'Quit', 'x':'Do X'}
    command = UserQueryCommandMenu(receiver, query_preface, query_dic)    

    response = command.Execute() 
    
    while response != 'q':
        
        match response:
            
            case 'x':
                do_X()
        
        print('--------------------')
        response = command.Execute() 

