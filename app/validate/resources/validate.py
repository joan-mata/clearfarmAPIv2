from flask import Flask, request

from app import msg_dict

from .. import validate_bp
from ..functions import validateUser

@validate_bp.route('/validate', methods=['POST'])
def validate():
    '''
    validate user within REST-API.
    
    Args: {
        login:  {   def: "Front-end user's login"
                    type: string,
                    required: For the user's search it is required,
                    default: 'none'
                    values: "any alphanumric in an string"                      
                }
        hash:   {   def: "Front-end user's password's hash"
                    type: string,
                    required: For the user's search it is required,
                    default: 'none'
                    values: "any alphanumric in an string"                      
                }                        
    }
    
    Return: {
        true: "If the user has been validated correctly"
        user_not_found: "Either the user is not found or the password is not correct",
    }
        
    '''
    if request.method=='POST':
        login, hash = recoveryForm.recoveryForm()

        print(f'login: {login} hash:{hash}') #debug
        #Check values we need
        #Values are required: login, hash
        validated = validateUser(login, hash)
        return validated if validated else msg_dict["user_not_found"] 

    return "Invalid request"
  

            
