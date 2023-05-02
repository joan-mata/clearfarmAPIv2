from app import db_cows

def welfareLastCow(disease, animalNum):
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
    data = list(db_cows["vet"].find({"official_cowID": animalNum},{"_id": 0, disease: 1,  "official_cowID": 1, "date": 1}))
    
    return_value = '0'
    date = [0, 0, 0] #[mm, dd, yy]
    item_date = [0, 0, 0] #[mm, dd, yy]
    for item in data:
        item_date[0] = int(item["date"][:2])
        item_date[1] = int(item["date"][3:5])
        item_date[2] = int(item["date"][6:])
        
        #analyze year
        if item_date[2] > date[2]:
            date[0] = item_date[0]
            date[1] = item_date[1]
            date[2] = item_date[2]
            return_value = item[disease]
        elif item_date[2] == date[2]:
            #analyze month
            if item_date[0] > date[0]:
                date[0] = item_date[0]
                date[1] = item_date[1]
                return_value = item[disease]
            elif item_date[0] == date[0]:
                #analyze day
                if item_date[1] > date[1]:
                    date[1] = item_date[1]
                    return_value = item[disease]
    
    return data
