from flask import request, Blueprint, Response
from Delivery import delivery_db as ddb
import json

delivery = Blueprint('delivery', __name__)

@delivery.route('/getDeliveryPDF',methods=['GET'])
def getDeliveryPDF():
    dtno = request.args.get('dtno')
    print(dtno)
    info = ddb.db_getDeliveryPDF(dtno)
    return json.dumps(info)

@delivery.route('/getDelivery',methods=['GET'])
def getDelivery():
    username = request.args.get('username')
    print(username)
    info = ddb.db_getDelivery(username)
    return json.dumps(info)

@delivery.route('/getDTExcel',methods=['GET'])
def getDTExcel():
    dtno = request.args.get('dtno')
    print(dtno)
    info = ddb.db_getDTExcel(dtno)
    return json.dumps(info)