import json
from flask import Flask, request, jsonify

from app import msg_dict

from .. import validate_bp
from ..functions import validateUser

@validate_bp.route('/validate', methods=['POST'])
def validate():
    '''
    validate user within REST-API.
    
    Args: {
        loginInfo: {  def: "Front-end user's login json"
                      type: json,
                      required: For the user's search it is required,
                      default: 'none'
                      fields:
                        user:{  def: "Front-end user's login"
                                type: string,
                                required: For the user's search it is required,
                                default: 'none'
                                values: "any alphanumric in an string"                      
                      }
                        hash:{  def: "Front-end user's password's hash"
                                type: string,
                                required: For the user's search it is required,
                                default: 'none'
                                values: "any alphanumric in an string"                      
                      }                        
                    }
    }                
    
    Return: {
        true: "If the user has been validated correctly"
        user_not_found: "Either the user is not found or the password is not correct",
    }
        
    '''
    print(1)
    if request.method == 'POST':
      print(2)
      print(f'content-type {request.content_type}')
      print(22)
      print(f'data {request.get_data()}')
      print(request)
      loginInfo = request.get_json()
      print(3)
      print(f"login: {loginInfo['user']} hash: {loginInfo['hash']}") #debug
      #Check values we need
      #Values are required: loginInfo
      validated = validateUser(loginInfo)
      return validated if validated else msg_dict["user_not_found"] 
    return msg_dict["request_method_error"]
  
  

            
