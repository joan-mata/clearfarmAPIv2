from app import db_cows

def welfareRangeCow(walfare, animalNum, timeFrom, timeTo):
    '''
    Search RANGE information about ONE cow
    
    Args: {
        walfare: {  def: ,
                    type: str,
                    values: ['health', 'feeding', 'housing', 'global']
                },
        animalNum: { def: "number for a one animal (or group of animals)",
                    type: int,
                    values: "any integer if it is greater than 0",
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
    
    WELFARE_VALUE = walfare + "_score"
    
    data = list(db_cows["welfare"].find({"cowID": animalNum},{"_id": 0, WELFARE_VALUE: 1,  "cowID": 1, "date": 1}))
    
    #Convert timeFrom
    date_from = [0, 0, 0] #[mm, dd, yy]
    date_from[0] = int(timeFrom[5:7])
    date_from[1] = int(timeFrom[8:])
    date_from[2] = int(timeFrom[2:4])

    #Convert timeTo
    date_to = [0, 0, 0] #[mm, dd, yy]
    date_to[0] = int(timeTo[5:7])
    date_to[1] = int(timeTo[8:])
    date_to[2] = int(timeTo[2:4])
    
    item_date = [0, 0, 0] #[mm, dd, yy]
    return_value = []
    
    for item in data:
        item_date[0] = int(item["date"][:2])
        item_date[1] = int(item["date"][3:5])
        item_date[2] = int(item["date"][6:])

        #analyze year from
        if item_date[2] > date_from[2]:
            #analyze year to
            if item_date[2] < date_to[2]:
                return_value.append(item)
            elif item_date[2] == date_to[2]:
                #analyze month to
                if item_date[0] < date_to[0]:
                    return_value.append(item)
                elif item_date[0] == date_to[0]:
                    #analyze day to
                    if item_date[1] <= date_to[1]:
                        return_value.append(item)
                
        elif item_date[2] == date_from[2]:
            #analyze month from
            if item_date[0] > date_from[0]:
                #analyze year to
                if item_date[2] < date_to[2]:
                    return_value.append(item)
                elif item_date[2] == date_to[2]:
                    #analyze month to
                    if item_date[0] < date_to[0]:
                        return_value.append(item)
                    elif item_date[0] == date_to[0]:
                        #analyze day to
                        if item_date[1] <= date_to[1]:
                            return_value.append(item)
                
            elif item_date[0] == date_from[0]:
                #analyze day from
                if item_date[1] >= date_from[1]:
                    #analyze year to
                    if item_date[2] < date_to[2]:
                        return_value.append(item)
                    elif item_date[2] == date_to[2]:
                        #analyze month to
                        if item_date[0] < date_to[0]:
                            return_value.append(item)
                        elif item_date[0] == date_to[0]:
                            #analyze day to
                            if item_date[1] <= date_to[1]:
                                return_value.append(item)

    return return_value
