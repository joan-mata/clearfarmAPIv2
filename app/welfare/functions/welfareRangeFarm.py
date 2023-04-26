from . import welfareRangeCow

from app import db_cows

def welfareRangeFarm(walfare, farmID, timeFrom, timeTo):
    '''
    Search ALL information about ONE farm
    
    Args: {
        walfare: {  def: ,
                    type: str,
                    values: ['health', 'feeding', 'housing', 'global']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    values: "any integer if it is greater than 0"
                },
        timeFrom: { def: "lower limit for the range of dates where we want to search information",
                    type: string,
                    format date: 'YYYY-MM-DD',
                    values: date,
                },
        timeTo: {   def: "upper limit for the range of dates where we want to search information",
                    type: string,
                    format date: 'YYYY-MM-DD',
                },
    }
    '''
    WALFARE_VALUE = walfare + "_score"
    
    list_cowId = list(db_cows["reference"].find({"farmID": farmID},{"_id": 0, "farmID": 1,  "cowID": 1}))

    data = []
    
    for item in list_cowId: #each item is a dictionary
        aux_data = welfareRangeCow.welfareRangeCow(walfare, item["cowID"], timeFrom, timeTo)
        
        #dict = {"cowID": item["cowID"], WALFARE_VALUE: score}
        #data.append(dict)
        data += aux_data
        
    return data
