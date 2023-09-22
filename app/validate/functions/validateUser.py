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
    print(f'validating hash from db user: {user}') #debug
    decoded_db_hash = user['password'].decode()
    print(f'decode: {decoded_db_hash}') #debug
    decoded_hex_db_hash = decoded_db_hash.hex()
    print(f'hex: {decoded_hex_db_hash}') #debug
    print(f"Are equal: {decoded_hex_db_hash == loginInfo['hash']}")

    validated = True if len(user) and user['password']==hash else False
    
    print(f"user hash input: {loginInfo['hash']}") #debug
    if len(user): #debug
      print(f"db hash: {user['password']}") #debug
      print(f"Are equal? {user['password'] == loginInfo['hash']}")#debug

    return validated