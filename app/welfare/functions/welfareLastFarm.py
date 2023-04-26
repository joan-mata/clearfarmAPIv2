from . import welfareLastCow

from app import db_cows

def welfareLastFarm(walfare, farmID):
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
        
    list_cowId = list(db_cows["reference"].find({"farmID": farmID},{"_id": 0, "farmID": 1,  "cowID": 1}))

    data = []
    for item in list_cowId: #each item is a dictionary
        print("cowID: " + str(item["cowID"]))
        aux_data = welfareLastCow.welfareLastCow(walfare, item["cowID"])
        print("aux_data: " + str(aux_data))
        data += aux_data
        
    return data
