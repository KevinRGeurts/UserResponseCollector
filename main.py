# Standard

# Local
from UserQueryCommand import UserQueryCommandMenu, UserQueryCommandPathSave
import UserQueryReceiver


def do_Debug():
    """
    Use UserResponseCollector to debug.
    """
    receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
    query_preface = 'Enter a valid file system path.'
    command = UserQueryCommandPathSave(receiver, query_preface)
        
    exp_val = 'None'
    test_path = command.Execute()
    act_val = str(test_path)

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
    query_dic = {'q':'Quit', 'd':'Debug'}
    command = UserQueryCommandMenu(receiver, query_preface, query_dic)    

    response = command.Execute() 
    
    while response != 'q':
        
        match response:
            
            case 'd':
                do_Debug()
        
        print('--------------------')
        response = command.Execute() 

