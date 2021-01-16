from flask import request,Blueprint,jsonify
from User import user_db as udb

user = Blueprint('user', __name__)

@user.route('/fetchUserName',methods=['POST'])
def fetchUserName():
    email = request.get_json()['usrname']
    return jsonify({
        'username' : udb.getUserName(email),
        'assetlist' : udb.getUserInfo(email)
    })

@user.route('/usertest',methods=['GET'])
def usertest():
    return 'usertest'


