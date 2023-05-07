from . import diseaseLastCow

from app import db_cows

def diseaseLastFarm(disease, farmID):
    '''
    Search LAST information about ONE farm
    
    Args: {
        walfare: {  def: ,
                    type: str,
                    values: ['health', 'feeding', 'housing', 'global']
        
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    values: "any integer if it is greater than 0"
                },
    }
    '''
    return_data = 'none'
    data = list(db_cows["vet"].find({"farmID": farmID},{"_id": 0, disease: 1,  "official_cowID": 1, "date": 1}))
        
    if data:
        return_data = []
        for item in data:
            if item[disease] != "":
                return_data.append(item)
    
    
    return return_data
