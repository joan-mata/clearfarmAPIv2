from flask import Flask, request, render_template

from app import msg_dict

from .. import insert_bp


@insert_bp.route('/insert/cow/', methods=['GET', 'POST'])
def insert():
    '''
    Insert data n REST-API.
    If mandatory you use POST method.
    
    Args: {
        enterprise: {
            def: "is the organism that provides the data.",
            type: string,
            required: yes,
            values: undefined
        },
        file: {
            def: "is the data.",
            type: string,
            required: yes,
            values: ['csv', 'json']
        },
        key: {
            def: "ID of this enterprise.",
            type: string,
            required: "depending (if your insert this enterprise for first time, 'key' is required",
            value: undefined
        }
    }
    
    Return: {
        error_no_post: "if you do not use POST method.",
        ok_insert: "if you insert the data correctly."
    }
    '''
    
    #value_return = msg_dict["error_no_post"]
    
    if request.method == 'POST':
        
        value_return = msg_dict["ok_insert"]
    
    
    return render_template('insert/insert.html')

            
