# Standard

# Local
from UserResponseCollector import UserResponseCollector_query_user, BlackJackQueryType


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
    query_preface = 'How do you want to use the workbench?'
    query_dic = {'q':'Quit', 'x':'Do X'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    
    while response != 'q':
        
        match response:
            
            case 'x':
                do_X()
        
        print('--------------------')
        response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)

