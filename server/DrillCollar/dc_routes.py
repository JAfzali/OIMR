from flask import request, Blueprint, Response
from DrillCollar import dc_db as ddb
import json
import fmrest

dc = Blueprint('dc', __name__)

@dc.route('/getdcPDF',methods=['GET'])
def getdcPDF():
    orderno = request.args.get('orderno')
    print(orderno)
    info = ddb.db_getdcPDF(orderno)
    return json.dumps(info)

@dc.route('/getdc',methods=['GET'])
def getdc():
    username = request.args.get('username')
    print(username)
    info = ddb.db_getdc(username)
    return json.dumps(info)