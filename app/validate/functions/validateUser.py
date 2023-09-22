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
    
    input_pwd_to_hex = bytes.fromhex(loginInfo['hash'])
    
    validated = True if len(user) and user['password']==input_pwd_to_hex else False
    
    return validated