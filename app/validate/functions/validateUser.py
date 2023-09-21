from . import searchUser
import base64

def validateUser(user, hash):
    '''
    Validates if the stored user's hash matches with the form-provided one
    
    :param user: the user's dictionary from the database
    :param hash: the user's password's hash encoded as base64
    :return: true if the stored user's password's hashcode matches with the 
    provided one.
    '''
    query_result = searchUser(user)

    validated = True if len(query_result) and query_result[0]['hash']==hash else False
    #decoded_input_hash = base64.b64decode(hash)
    print(f'user hash input: {hash}') #debug
    if len(query_result):
      print('db hash: {}'.format(query_result[0]['hash'])) #debug
      print('Are equal? {}'.format(query_result[0]['hash']==hash))#debug

    return validated