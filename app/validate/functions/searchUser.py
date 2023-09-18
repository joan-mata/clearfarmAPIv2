from app import db_users

# Flask Searches User
def searchUser(login):
    '''
    Search by user
    
    :param login: the user's login
    :param hash: the user's password's hash
    :return: true if the user's password's hashcode 
    '''
    query_result = list(db_users["admin"].find({'user': login}))
    user = query_result[0] if len(query_result) else {}
return user