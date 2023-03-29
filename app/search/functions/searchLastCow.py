from app import db_cows

def searchLastCow(farmID, cowNum, id):
    '''
    Search LAST information about ONE cow
    
    Args:
        None
    '''
    
    #find id's in reference collection
    referenceIds = list(db_cows["reference"].find({"$and":[{"farmID": farmID},{id: cowNum}]}).sort("$natural", -1))
            
    if referenceIds:
        referenceIds = referenceIds[0]
    else:
        error = {
            "type": "error",
            "name": "error_value_animalId",
            "text": "It is possible that you have not correctly selected the 'AnimalId' value.",
        }
        return error
    
    #recovery collections - id matrix (list of dictionarys)
    matrix = list(db_cows["listCollections"].find({"collection": {"$exists": "true"}}))

    data = []
    for item in matrix: #each item is a dictionary
        #item values
        itemCollection = item["collection"]
        itemId = item["key"]

        #referenceIds values
        referenceFarmId = referenceIds["farmID"]
        referenceCowNum = referenceIds[itemId]
        
        temporalData = list(db_cows[itemCollection].find({"$and":[{"farmID": referenceFarmId},{itemId: referenceCowNum}]}).sort("$natural", -1))
        if temporalData:
            data.append(temporalData[0])

    return data
