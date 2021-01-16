from flask import request, Blueprint, Response
from OCTG import octg_db as odb
import json
import fmrest

octg = Blueprint('octg', __name__)

@octg.route('/getoctgPDF',methods=['GET'])
def getoctgPDF():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getoctgPDF(orderno)
    return json.dumps(info)

@octg.route('/getoctg',methods=['GET'])
def getoctg():
    username = request.args.get('username')
    print(username)
    info = odb.db_getoctg(username)
    return json.dumps(info)