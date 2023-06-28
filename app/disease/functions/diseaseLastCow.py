from app import db_cows

def diseaseLastCow(disease, animalNum):
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
    return_data = 'none'
    data = list(db_cows["vet"].find({"official_cowID": animalNum},{"_id": 0, disease: 1,  "official_cowID": 1, "dateStart": 1}))
    
    #data["dateStart"] -> format "mm/dd/yyyy"
    
    date = [0, 0, 0] #[mm, dd, yy]
    item_date = [0, 0, 0] #[mm, dd, yy]
    for item in data:
        if item[disease] != "":

            date_aux = item["dateStart"]
            
            value1 = date_aux.index("/")
            value2 = date_aux[value1+1:].index("/") + value1 + 1
            
            item_date[0] = int(date_aux[:value1])
            item_date[1] = int(date_aux[value1+1:value2])
            item_date[2] = int(date_aux[value2+1:])

            #analyze year
            if item_date[2] > date[2]:
                date[0] = item_date[0]
                date[1] = item_date[1]
                date[2] = item_date[2]
                return_data = item[disease]
            elif item_date[2] == date[2]:
                #analyze month
                if item_date[0] > date[0]:
                    date[0] = item_date[0]
                    date[1] = item_date[1]
                    return_data = item[disease]
                elif item_date[0] == date[0]:
                    #analyze day
                    if item_date[1] > date[1]:
                        date[1] = item_date[1]
                        return_data = item[disease]
    
    return return_data
