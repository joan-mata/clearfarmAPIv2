from flask import Flask, request

from .. import welfare_index_bp
from ..functions import funct_welfare_index

@welfare_index_bp.route('/welfare_index/score')
def wf_index():
    '''
    Search and return data range for GLOBAL score of an animal.

    Args: {
        farmId: {   def: number of farm where we want search this animal,
                    type: int,
                    required: yes,
                    default: 0,
                    values: "any integer if it is greater than 0"
                },
        timeTo: {   def: "upper limit for the range of dates where we want to search information",
                    type: string,
                    required: no,
                    format date: 'YYYY-MM-DD',
                    default: 'none',
                    values: "any date greater than 'timeFrom' and smaller than today",
                    comment: "If you do not insert any value in 'timeFrom', the 'timeTo' does not work."
                },
    }
    '''

    farmId = str(request.args.get('farmId', default=0, type=int))
    timeTo = request.args.get('timeTo', default='none', type=str)

    value_return = funct_welfare_index.funct_welfare_index(farmId, timeTo)
    print(value_return)
    return value_return