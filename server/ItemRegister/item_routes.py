from flask import request, Blueprint, Response
from ItemRegister import item_db as idb
import json

item = Blueprint('item', __name__)


@item.route('/itemtest',methods=['GET'])
def itemtest():
    return 'itemtest'

@item.route('/getInventory',methods=['GET'])
def getInventory():
    username = request.args.get('username')
    print(username)
    info = idb.db_getInventory(username)
    return json.dumps(info)





