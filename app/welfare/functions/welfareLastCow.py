from app import db_cows

def welfareLastCow(walfare, animalNum):
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
    walfare_value = walfare + "_score"
    
    data = list(db_cows["welfare"].find({"cowID": animalNum},{"_id": 0, walfare_value: 1,  "cowID": 1, "date": 1}))
    
    date = [0, 0, 0] #[mm, dd, yyyy]
    for item in data:
        item_date[0] = int(item["date"][:2])
        item_date[1] = int(item["date"][3:4])
        item_date[2] = int(item["date"][5:])
        
        print(item["date"])
        print(item_date[0])
        print(item_date[1])
        print(item_date[2])
        
    
    
#    #find id's in reference collection
#    referenceIds = list(db_cows["reference"].find({"$and":[{"farmID": farmId},{'cowId': cowNum}]}).sort("$natural", -1))
#
#    if referenceIds:
#        referenceIds = referenceIds[0]
#    else:
#        error = {
#            "type": "error",
#            "name": "error_value_animalId",
#            "text": "It is possible that you have not correctly selected the 'AnimalId' value.",
#        }
#        return error
#
#    #recovery collections - id matrix (list of dictionarys)
#    matrix = list(db_cows["listCollections"].find({"collection": {"$exists": "true"}}))
#
#    data = []
#    for item in matrix: #each item is a dictionary
#        #item values
#        itemCollection = item["collection"]
#        itemId = item["key"]
#
#        #referenceIds values
#        referenceFarmId = referenceIds["farmID"]
#        referenceCowNum = referenceIds[itemId]
#
#        temporalData = list(db_cows[itemCollection].find({"$and":[{"farmID": referenceFarmId},{itemId: referenceCowNum}]}).sort("$natural", -1))
#        if temporalData:
#            data.append(temporalData[0])

    return data
