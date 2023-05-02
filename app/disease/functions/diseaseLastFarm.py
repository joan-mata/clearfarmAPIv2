from . import diseaseLastCow

from app import db_cows

def diseaseLastFarm(walfare, farmID):
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
    WELFARE_VALUE = walfare + "_score"
    
    list_cowId = list(db_cows["reference"].find({"farmID": farmID},{"_id": 0, "farmID": 1,  "cowID": 1}))

    data = []
    
    for item in list_cowId: #each item is a dictionary
        score = diseaseLastCow.diseaseLastCow(walfare, item["cowID"])
        
        dict = {"cowID": item["cowID"], WELFARE_VALUE: score}
        data.append(dict)
        
    return data
