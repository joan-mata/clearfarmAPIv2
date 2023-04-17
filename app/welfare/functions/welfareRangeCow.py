from . import compareDate
from app import db_cows

def welfareRangeCow(farmID, animalNum, timeFrom, timeTo):
    '''
    
    Args:
        None
    '''
    
    #treat dates
        #Format time: YYYY-MM-DD (String)
        #Format date: [YYYY, MM, DD] (List of Int)
        #Format timeDb: MM/DD/YYYY (String)
    dateFrom = []
    dateFrom.append(int(timeFrom[:4]))
    dateFrom.append(int(timeFrom[5:7]))
    dateFrom.append(int(timeFrom[8:]))
    
    if timeTo != "":
        dateTo = []
        dateTo.append(int(timeTo[:4]))
        dateTo.append(int(timeTo[5:7]))
        dateTo.append(int(timeTo[8:]))
    else:
        dateTo = ""
    
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
        
        #TODO: Comprobar si devuelve un diccionario o se ha de hacer una lista por narices
        data = db_cows["walfare"].find({"health_score": {"$exists": "true"}})
        
        for temporalItem in temporalData:
            timeDb = temporalItem['date_insert_in_db']
            #TODO: hay que cambiarle el formato de MM/DD/YYYY a DD-MM-YYYY o cambiar el compareDate
            flag = compareDate.compareDate(dateFrom, dateTo, temporalItem['date_insert_in_db'])
            
            if temporalData and flag:
                data.append(temporalItem)

    return data

