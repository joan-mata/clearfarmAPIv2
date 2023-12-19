from app import db_cows

from datetime import datetime, timedelta


def welfareIndex(farmID, timeTo):
    '''
    Search ALL information about ONE farm

    Args: {
        welfare: {  def: ,
                    type: str,
                    values: ['health', 'feeding', 'housing', 'global']
                },
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    values: "any integer if it is greater than 0"
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

    timeTo = datetime.strptime(timeTo, '%Y-%m-%d')
    timeFrom = (timeTo - timedelta(days=14)).strftime('%Y-%m-%d')
    timeTo = timeTo.strftime('%Y-%m-%d')

    print(type(timeFrom))
    print(timeFrom)
    pipeline = [
        {
            "$match": {
                "farmID": int(farmID),
                "dateStart": {"$gte": timeFrom, "$lte": timeTo}
            }
        },
        {
            "$group": {
                "_id": None,  # Grouping all documents together
                "average_welfare": {"$avg": "$score"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "average_welfare": 1
            }
        }
    ]

    data = list(db_cows["welfare_idx"].aggregate(pipeline))

    return data
