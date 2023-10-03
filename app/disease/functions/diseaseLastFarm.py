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
    data = list(db_cows["vet"].find({"farmID": farmID, "dateStart": '10/31/2022'},{"_id": 0, disease: 1,  "official_cowID": 1, "dateStart": 1}))
      
    return_data = []
    
    # for item in data: #each item is a dictionary
    #     if item[disease] != "":
    #         disease_value = diseaseLastCow.diseaseLastCow(disease, item["official_cowID"])
            
    #         dict = {"official_cowID": item["official_cowID"], disease: disease_value}
    #         return_data.append(dict)
    
    return return_data
