from flask import Flask, request

from .. import disease_bp
from ..functions import funct_disease
    
@disease_bp.route('/disease/mastitis')
def disease_mastitis():
    '''
    Search and return data range for MASTITIS disease of animal
    
    Args: {
        animal: {   def: "is the type of animal we want search.",
                    type: string,
                    required: yes,
                    default: 'none',
                    values: ['cow', 'pig']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: str,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalNum = request.args.get('animalNum', default = 'none', type = str)
    
    value_return = funct_disease.funct_disease("mastitis", animal, farmId, animalNum)
    
    return value_return
            
@disease_bp.route('/disease/acidosis')
def disease_acitosis():
    '''
        Search and return data range for ACIDOSIS disease of animal
    
    Args: {
        animal: {   def: "is the type of animal we want search.",
                    type: string,
                    required: yes,
                    default: 'none',
                    values: ['cow', 'pig']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: str,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalNum = request.args.get('animalNum', default = 'none', type = str)
    
    value_return = funct_disease.funct_disease("acidosis", animal, farmId, animalNum)
    
    return value_return

@disease_bp.route('/disease/pneumonia')
def disease_pneumonia():
    '''
        Search and return data range for PNEUMONIA disease of animal
    
    Args: {
        animal: {   def: "is the type of animal we want search.",
                    type: string,
                    required: yes,
                    default: 'none',
                    values: ['cow', 'pig']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: str,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalNum = request.args.get('animalNum', default = 'none', type = str)
    
    value_return = funct_disease.funct_disease("pneumonia", animal, farmId, animalNum)
    
    return value_return
    
@disease_bp.route('/disease/abomasus_surgery')
def disease_abomasus_surgery():
    '''
        Search and return data range for ABOMASUS SURGERY disease of animal
    
    Args: {
        animal: {   def: "is the type of animal we want search.",
                    type: string,
                    required: yes,
                    default: 'none',
                    values: ['cow', 'pig']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: str,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalNum = request.args.get('animalNum', default = 'none', type = str)
    
    value_return = funct_disease.funct_disease("abomasus_surgery", animal, farmId, animalNum)
    
    return value_return

@disease_bp.route('/disease/all')
def disease_all():
    '''
    Search and return data range for ALL disease of animal
    
    Args: {
        animal: {   def: "is the type of animal we want search.",
                    type: string,
                    required: yes,
                    default: 'none',
                    values: ['cow', 'pig']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: str,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    
    animal = request.args.get('animal', default = 'none', type = str)
    farmId = str(request.args.get('farmId', default = 0, type = int))
    animalNum = request.args.get('animalNum', default = 'none', type = str)
    timeFrom = request.args.get('timeFrom', default = 'none', type = str)
    
    
    disease = ["mastitis", "acidosis", "pneumonia", "abomasus_surgery"]
    value_return = []
    
    for item in disease:
        aux_data = funct_disease.funct_disease(item, animal, farmId, animalNum)
        dict = {item: aux_data}
        value_return.append(dict)
    
    return value_return
