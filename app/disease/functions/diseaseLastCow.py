from app import db_cows

def diseaseLastCow(disease, animalNum):
    '''
    Search LAST information about ONE cow
    
    Args: {
        walfare: {  def: ,
                    type: str,
                    values: ['health', 'feeding', 'housing', 'global']
        
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: int,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    return_data = 'none'
    data = list(db_cows["vet"].find({"official_cowID": animalNum},{"_id": 0, disease: 1,  "official_cowID": 1, "date": 1}))
    
    if data:
        return_data = []
        for item in data:
            if item[disease] != "":
                return_data.append(item[disease])
    
    
    return return_data
