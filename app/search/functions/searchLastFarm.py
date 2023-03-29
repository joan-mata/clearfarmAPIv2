from app import db_cows

def searchLastFarm(farmID):
    '''
    Search LAST information about ONE farm
    
    Args:
        None
    '''
        
    #recovery collections - id matrix (list of dictionarys)
    matrix = list(db_cows["listCollections"].find({"collection": {"$exists": "true"}}))

#    data = []
    data = {}
    index = 0
    for item in matrix: #each item is a dictionary
        #item values
        itemCollection = item["collection"]

        temporalData = list(db_cows[itemCollection].find({"farmID": farmID}).sort("$natural", -1))
        
        if temporalData:
#            data.append(temporalData[0])
            data.update({str(index): temporalData[0]})
            index += 1

    print("DATA " + str(type(data)))

    return data
