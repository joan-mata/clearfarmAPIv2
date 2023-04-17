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
    walfare_value = walfare + "_score"
    
    data = list(db_cows["welfare"].find({"cowID": animalNum},{"_id": 0, walfare_value: 1,  "cowID": 1, "date": 1}))
    
    date_from = [0, 0, 0] #[mm, dd, yy]
    date_from[0] = int(timeFrom[5:7])
    date_from[1] = int(timeFrom[8:])
    date_from[2] = int(timeFrom[2:4])
    
    date_to = [0, 0, 0] #[mm, dd, yy]
    date_to[0] = int(timeTo[5:7])
    date_to[1] = int(timeTo[8:])
    date_to[2] = int(timeTo[2:4])
    
    print("TimeFrom: " + str(date_from))
    print("TimeTo: " + str(date_to))
    
    item_date = [0, 0, 0] #[mm, dd, yy]
#    for item in data:
#        item_date[0] = int(item["date"][:2])
#        item_date[1] = int(item["date"][3:5])
#        item_date[2] = int(item["date"][6:])
#
#        #analyze year
#        if item_date[2] > date[2]:
#            date[0] = item_date[0]
#            date[1] = item_date[1]
#            date[2] = item_date[2]
#            score = item[walfare_value]
#        elif item_date[2] == date[2]:
#            #analyze month
#            if item_date[0] > date[0]:
#                date[0] = item_date[0]
#                date[1] = item_date[1]
#                score = item[walfare_value]
#            elif item_date[0] == date[0]:
#                #analyze day
#                if item_date[1] > date[1]:
#                    date[1] = item_date[1]
#                    score = item[walfare_value]
    

    return score
