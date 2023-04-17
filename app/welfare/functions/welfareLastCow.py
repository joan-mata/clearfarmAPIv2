from app import db_cows

def welfareLastCow(walfare, farmId, animalNum):
    '''
    Search LAST information about ONE cow
    
    Args: {
        walfare: {  def: ,
                    type: str,
                    values: ['health', 'feeding', 'housing', 'global']
        
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    values: "any integer if it is greater than 0"
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: int,
                    required: no,
                    default: 0,
                    values: "any integer if it is greater than 0",
                },
    }
    '''
    walfare_value = walfare + "_score"
    
    data = db_cows["welfare"].find({"cowID": "44341"},{"_id": 0, walfare_value: 1,  "cowID": 1, "date": 1})
    
    
    print("Type: " + str(type(data)))
    print("DATA: ")
    print(data)
    
    
    
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
