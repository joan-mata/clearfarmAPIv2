from . import searchUser

def validateUser(user, hash):
    '''
    Validates if the stored user's hash matches with the form-provided one
    
    :param user: the user's dictionary from the database
    :param hash: the user's password's hash specified through a login form
    :return: true if the stored user's password's hashcode matches with the 
    provided one.
    '''
    query_result = searchUser(user)
    validated = true if len(query_result) and query_result[0]['hash']==hash else false
return validated