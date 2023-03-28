from app import db_cows

# Flask Searches Farm
def searchAllFarm(farmID):
    '''
    Search ALL information about ONE farm
    
    Args:
        None
    '''
        
    #recovery collections - id matrix (list of dictionarys)
    matrix = list(db_cows["listCollections"].find({"collection": {"$exists": "true"}}))

    data = []
    for item in matrix: #each item is a dictionary
        #item values
        itemCollection = item["collection"]

        temporalData = list(db_cows[itemCollection].find({"farmID": farmID}).sort("$natural", -1))
        if temporalData:
            data.append(temporalData)
            
    return data
