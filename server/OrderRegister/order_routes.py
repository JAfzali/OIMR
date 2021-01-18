from flask import request, Blueprint, Response
from OrderRegister import order_db as odb
import json

order = Blueprint('order', __name__)

@order.route('/ordertest',methods=['GET'])
def ordertest():
    return 'ordertest'

@order.route('/getOrderconfirm',methods=['GET'])
def getOrderconfirm():
    username = request.args.get('username')
    print(username)
    info = odb.db_getOrderconfirm(username)
    return json.dumps(info)

@order.route('/getOrderPDF',methods=['GET'])
def getOrderPDF():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getOrderpdf(orderno)
    return json.dumps(info)

@order.route('/getMachExcel',methods=['GET'])
def getMachExcel():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getMachExcel(orderno)
    return json.dumps(info)

@order.route('/getHardExcel',methods=['GET'])
def getHardExcel():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getHardExcel(orderno)
    return json.dumps(info)

@order.route('/getHardExcelHW',methods=['GET'])
def getHardExcelHW():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getHardExcelHW(orderno)
    return json.dumps(info)


@order.route('/getMachExcelHW',methods=['GET'])
def getMachExcelHW():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getMachExcelHW(orderno)
    return json.dumps(info)

@order.route('/getMachExcelDC',methods=['GET'])
def getMachExcelDC():
    orderno = request.args.get('orderno')
    print(orderno)
    info = odb.db_getMachExcelDC(orderno)
    return json.dumps(info)





