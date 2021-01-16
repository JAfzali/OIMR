from flask import request, Blueprint, Response
from DrillPipe import dp_db as ddb
import json
import fmrest

dp = Blueprint('dp', __name__)

@dp.route('/getdpPDF',methods=['GET'])
def getdpPDF():
    orderno = request.args.get('orderno')
    print(orderno)
    info = ddb.db_getdpPDF(orderno)
    return json.dumps(info)

@dp.route('/getdp',methods=['GET'])
def getdp():
    username = request.args.get('username')
    print(username)
    info = ddb.db_getdp(username)
    return json.dumps(info)

@dp.route('/getdpExcel',methods=['GET'])
def getdpExcel():
    orderno = request.args.get('orderno')
    print(orderno)
    info = ddb.db_getdpExcel(orderno)
    return json.dumps(info)