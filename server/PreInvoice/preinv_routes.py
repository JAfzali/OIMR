from flask import request, Blueprint, Response
from PreInvoice import preinv_db as pdb
import json

preinv = Blueprint('preinv', __name__)

@preinv.route('/getPreinvPDF',methods=['GET'])
def getPreinvPDF():
    orderno = request.args.get('orderno')
    print(orderno)
    info = pdb.db_getPreinvPDF(orderno)
    return json.dumps(info)

@preinv.route('/getPreinv',methods=['GET'])
def getPreinv():
    username = request.args.get('username')
    print(username)
    info = pdb.db_getPreinv(username)
    return json.dumps(info)



