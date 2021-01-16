from flask import request, Blueprint, Response
from ReceivedRegister import received_db as rdb
import json

received = Blueprint('received', __name__)

@received.route('/getReceivedPDF',methods=['GET'])
def getReceivedPDF():
    receivednr = request.args.get('receivednr')
    print(receivednr)
    info = rdb.db_getReceivedpdf(receivednr)
    return json.dumps(info)

@received.route('/getReceived',methods=['GET'])
def getReceived():
    username = request.args.get('username')
    print(username)
    info = rdb.db_getReceived(username)
    return json.dumps(info)





