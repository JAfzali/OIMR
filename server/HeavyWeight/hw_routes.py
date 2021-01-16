from flask import request, Blueprint, Response
from HeavyWeight import hw_db as hdb
import json
import fmrest

hw = Blueprint('hw', __name__)

@hw.route('/gethwPDF',methods=['GET'])
def gethwPDF():
    orderno = request.args.get('orderno')
    print(orderno)
    info = hdb.db_gethwPDF(orderno)
    return json.dumps(info)

@hw.route('/gethw',methods=['GET'])
def gethw():
    username = request.args.get('username')
    print(username)
    info = hdb.db_gethw(username)
    return json.dumps(info)