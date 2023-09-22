from . import searchUser

def validateUser(loginInfo):
    '''
    Validates if the stored user's hash matches with the form-provided one
    
    :param loginInfo: Json including the user login and password's hash.
    :return: True if the stored user's password's hashcode matches with the 
    provided one, False otherwise.
    '''
    validated = False
    user = searchUser.searchUser(loginInfo['user'])
    print(f'db_ user {user}')
    if len(user):
      input_pwd_to_hex = bytes.fromhex(loginInfo['hash'])
      #input_pwd_to_hex = loginInfo['hash']

      print(f"Are equal: \n {input_pwd_to_hex} \n {user['password']} \n {user['password'] == input_pwd_to_hex}")
     
      validated = True if len(user) and user['password']==input_pwd_to_hex else False
    
    return validated