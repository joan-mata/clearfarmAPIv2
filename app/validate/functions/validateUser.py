from . import searchUser
import base64

def validateUser(loginInfo):
    '''
    Validates if the stored user's hash matches with the form-provided one
    
    :param loginInfo: Json including the user login and password's hash.
    :return: True if the stored user's password's hashcode matches with the 
    provided one, False otherwise.
    '''
    user = searchUser.searchUser(loginInfo['user'])

    validated = True if len(user) and user['hash']==hash else False
    #decoded_input_hash = base64.b64decode(hash)
    print(f"user hash input: {loginInfo['hash']}") #debug
    if len(user): #debug
      print(f"db hash: {user['hash']}") #debug
      print(f"Are equal? {user['hash'] == loginInfo['hash']}")#debug

    return validated