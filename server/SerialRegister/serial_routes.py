from flask import request,Blueprint,jsonify,send_file,Response
from User import user_db as udb
from SerialRegister import serial_db as sdb
import json,os

serial = Blueprint('serial', __name__)


@serial.route('/serialtest',methods=['POST'])
def serialtest():
    username = request.get_json()['usrname']
    return username

@serial.route('/getPipesAndRacks',methods=['GET'])
def getPipesAndRacks():
    username = request.args.get('username')
    #username = request.get_json()['username']
    print(username)
    info = sdb.getPipesAndRacks(username)
    return json.dumps(info)

@serial.route('/getAllRacks',methods=['GET'])
def getAllRacks():
    username = request.args.get('username')
    #username = request.get_json()['username']
    print(username)
    info = sdb.getAllRacks()
    return json.dumps(info)

@serial.route('/getDataAsJson',methods=['GET'])
def getDataAsJson():
    username = 'OCEAN IMR AS'
    info = sdb.getPipesAndRacks(username)

    return Response(str(json.dumps(info, indent=4, sort_keys=True)),
                    mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=kcad.json'})

@serial.route('/showPipelist',methods=['GET'])
def showPipelist():
    itemnr = request.args.get('itemnr')
    print(itemnr)
    info = sdb.db_showList(itemnr)
    return json.dumps(info)

@serial.route('/showOtherlist',methods=['GET'])
def showOtherlist():
    itemnr = request.args.get('itemnr')
    location = request.args.get('location')
    print(itemnr)
    info = sdb.db_showOtherlist(itemnr,location)
    return json.dumps(info)

@serial.route('/getRack',methods=['GET'])
def getRack():
    rackname = request.args.get('rackname')
    print(rackname)
    info = sdb.db_getRack(rackname)
    return json.dumps(info)

@serial.route('/getPipes',methods=['GET'])
def getPipes():
    rackname = request.args.get('rackname')
    print(rackname)
    info = sdb.db_getPipes(rackname)
    return json.dumps(info)







