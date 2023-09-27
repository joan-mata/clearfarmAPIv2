from . import searchUser

def validateUser(loginInfo):
    '''
    Validates if the stored user's hash matches with the form-provided one
    
    :param loginInfo: Json including the user login and password's hash.
    :return: a dictionary {found: 1/0, validated: 1/0 } indicating if the 
    user has been found (1) and if the stored user's password's hashcode matches with the 
    provided one (1).
    '''
    result = {'found': 0, 'validated': 0}
    user = searchUser.searchUser(loginInfo['user'])
    print(f'db_ user {user}')
    if len(user):
      input_pwd_to_hex = bytes.fromhex(loginInfo['hash'])
      #input_pwd_to_hex = loginInfo['hash']

      print(f"Are equal: \n {input_pwd_to_hex} \n {user['password']} \n {user['password'] == input_pwd_to_hex}")

      result['found']=1
      if user['password']==input_pwd_to_hex :
        result['validated'] = 1
        result['user'] = user['user']
        result['farmID'] = user['farmID']
        result['scope'] = user['scope']
    
    return result