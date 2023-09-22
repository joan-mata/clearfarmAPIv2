from . import searchUser
import base64

def validateUser(loginInfo):
    '''
    Validates if the stored user's hash matches with the form-provided one
    
    :param loginInfo: Json including the user login and password's hash.
    :return: True if the stored user's password's hashcode matches with the 
    provided one, False otherwise.
    '''
    query_result = searchUser.searchUser(loginInfo['user'])

    validated = True if len(query_result) and query_result[0]['hash']==hash else False
    #decoded_input_hash = base64.b64decode(hash)
    print(f"user hash input: {loginInfo['hash']}") #debug
    if len(query_result):
      print(f"db hash: {query_result[0]['hash']}") #debug
      print(f"Are equal? {query_result[0]['hash'] == loginInfo['hash']}")#debug

    return validated