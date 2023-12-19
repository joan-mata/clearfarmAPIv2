from flask import Flask, request

from app import db_cows
from app import msg_dict

from .. import welfare_index_bp
from ..functions import welfareIndex


def funct_welfare_index(farmId, timeTo):
    # Check values to farmId
    if int(farmId) <= 0:
        if farmId == "0":
            return msg_dict["error_required_farmId"]
        else:
            return msg_dict["error_value_farmId"]

    return welfareIndex.welfareIndex(farmId, timeTo)
