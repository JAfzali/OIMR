from flask import Blueprint,request,jsonify,make_response,json
from Filemaker.connection import Filemaker
from User import user_db
import operator


serialDB = Filemaker('ODP_Serial_Number_Register_Info')


def divide_chunks(l, n):
    # looping till length l
    for i in reversed(range(0, len(l), n)):
        yield l[i:i + n]



def getPipesAndRacks(username):
    serialDB.conn.layout = 'ODP_Serial_Number_Register_Info'
    serialDB.conn.login()
    findquery = [
        { "Customer": f"=={username}","Rack_Position": "=Rack"},
        { "Position": "==","omit" : "true"}
]
    sortby = [
    {"fieldName": "Customer","sortOrder": "ascend"}]

    try:

        foundset = serialDB.conn.find(findquery, sortby, limit=1000)
    except Exception as e:
        print('error er ',e)
        serialDB.conn.logout()
        return json.dumps({'message' : 'Could not fetch racks and pipes'})
    serialDB.conn.logout()
    finaldict = {}
    rackset = set()
    for record in foundset:
        rackset.add(record.Rack_Position)

    for rack in rackset:
        finaldict[rack] = []

    for record in foundset:
        finaldict[record.Rack_Position].append(record.to_dict(ignore_portals=True))

    for x in finaldict:
        finaldict[x].sort(key=operator.itemgetter('Position'))


    for rack in rackset:
        serialDB.conn.layout = 'ODP_Rack_Location'
        serialDB.conn.login()
        findquery = [
            {"Rack_ID": f"=={rack}"}
        ]
        sortby = [
            {"fieldName": "Rack_ID", "sortOrder": "ascend"}]
        try:
            foundset1 = serialDB.conn.find(findquery, sortby, limit=1)
        except Exception as e:
            print('error er ', e)
            serialDB.conn.logout()
            return json.dumps({'message': 'Could not fetch rowcount'})
        serialDB.conn.logout()
        n = foundset1[0].Maxrowcount

        finaldict[rack] = list(divide_chunks(finaldict[rack],n))

    return finaldict

def getAllRacks():
    serialDB.conn.layout = 'ODP_Serial_Number_Register_Info'
    serialDB.conn.login()
    findquery = [
        {"Rack_Position": "==", "omit": "true"},
        {"Position": "==", "omit": "true"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "ascend"}]

    try:

        foundset = serialDB.conn.find(findquery, sortby, limit=1000)
    except Exception as e:
        print('error er ', e)
        serialDB.conn.logout()
        return json.dumps({'message': 'Could not fetch racks and pipes'})
    serialDB.conn.logout()
    finaldict = {}
    rackset = set()
    for record in foundset:
        rackset.add(record.Rack_Position)

    for rack in rackset:
        finaldict[rack] = []

    for record in foundset:
        finaldict[record.Rack_Position].append(record.to_dict(ignore_portals=True))

    for x in finaldict:
        finaldict[x].sort(key=operator.itemgetter('Position'))


    for rack in rackset:
        serialDB.conn.layout = 'ODP_Rack_Location'
        serialDB.conn.login()
        findquery = [
            {"Rack_ID": f"=={rack}"}
        ]
        sortby = [
            {"fieldName": "Rack_ID", "sortOrder": "ascend"}]
        try:
            foundset1 = serialDB.conn.find(findquery, sortby, limit=1)
        except Exception as e:
            print('error er ', e)
            serialDB.conn.logout()
            return json.dumps({'message': 'Could not fetch rowcount'})
        serialDB.conn.logout()
        n = foundset1[0].Maxrowcount


        emptylist = list(divide_chunks(finaldict[rack], n)) #empty.append
        finaldict[rack] = []
        finaldict[rack].append(emptylist)
        rackinfo = foundset1[0].to_dict()
        finaldict[rack].append(rackinfo)
    return finaldict

def db_showList(itemnr):
    serialist = []
    serialDB.conn.layout = 'temp_serial_reg'
    serialDB.conn.login()
    findquery = [{"Item_No": f"=={itemnr}", "Current_Location": "=Rig Ready"}]
    sortby = [{"fieldName": "Position", "sortOrder": "ascend"}]

    try:
        foundset = serialDB.conn.find(findquery, sortby, limit=1000)
    except Exception as e:
        print('error er ',e)
        serialDB.conn.logout()
        return json.dumps({'message' : 'Could not fetch serial number list'}),401
    serialDB.conn.logout()

    for record in foundset:
        serialist.append(record.to_dict(ignore_portals=True))
    return serialist

def db_showOtherlist(itemnr,location):
    serialist = []
    serialDB.conn.layout = 'temp_serial_reg'
    serialDB.conn.login()
    findquery = [{"Item_No": f"=={itemnr}", "Current_Location": f"={location}"}]
    sortby = [{"fieldName": "Position", "sortOrder": "ascend"}]

    try:
        foundset = serialDB.conn.find(findquery, sortby, limit=1000)
    except Exception as e:
        print('error er ',e)
        serialDB.conn.logout()
        return json.dumps({'message' : 'Could not fetch serial number list'}),401
    serialDB.conn.logout()

    for record in foundset:
        serialist.append(record.to_dict(ignore_portals=True))
    return serialist




#This method only collects rackdata for a rack
def db_getRack(rackname):
    #Get racks
    Rackdict = dict()
    pipelist = []


    serialDB.conn.layout = 'ODP_Rack_Info'
    serialDB.conn.login()
    findquery_rack = [{"Rack_ID": f"=={rackname}"}]
    try:
        foundset = serialDB.conn.find(findquery_rack, limit=1)
    except Exception as e:
        print('error er ', e)
        serialDB.conn.logout()
        return json.dumps({'message': 'Could not find rack'}),401
    serialDB.conn.logout()
    Rackdict['rackinfo'] = foundset[0].to_dict()
    return Rackdict



def db_getPipes(rackname):
    Rackdict = dict()
    pipelist = []
    colormap = dict()


    #INFO RACK
    serialDB.conn.layout = 'ODP_Rack_Info'
    serialDB.conn.login()
    findquery_rack = [{"Rack_ID": f"=={rackname}"}]
    try:
        foundset1 = serialDB.conn.find(findquery_rack, limit=1)
    except Exception as e:
        print('error er ', e)
        serialDB.conn.logout()
        return json.dumps({'message': 'Could not find rack'}),401
    serialDB.conn.logout()
    Rackdict['rackinfo'] = foundset1[0].to_dict()
    Rackdict['rackinfo']['Rack_ID'] = Rackdict['rackinfo']['Rack_ID'].replace("_", " ")


    #INFO PIPES
    serialDB.conn.layout = 'temp_serial_reg'
    serialDB.conn.login()
    findquery_pipe = [
        {"Rack_Position": f"=={rackname}"},
        {"Position": "==", "omit": "true"}
    ]
    sortby = [
        {"fieldName": "Position", "sortOrder": "ascend"}]
    try:
        foundset2 = serialDB.conn.find(findquery_pipe, sortby, limit=1000)
    except Exception as e:
        print('error er ', e)
        serialDB.conn.logout()
        return json.dumps({'message': 'Could not fetch serial number list'}), 401
    serialDB.conn.logout()
    for record in foundset2:
        pipelist.append(record.to_dict(ignore_portals=True))
    Rackdict['pipes'] = pipelist

    #COLOR MAP
    if Rackdict['rackinfo']['Item_Number'] != ' ':
        colormap[Rackdict['rackinfo']['Item_Number']] = Rackdict['rackinfo']['color1']
    if Rackdict['rackinfo']['Item_Number_2'] != ' ':
        colormap[Rackdict['rackinfo']['Item_Number_2']] = Rackdict['rackinfo']['color2']
    if Rackdict['rackinfo']['Item_Number_3'] != ' ':
        colormap[Rackdict['rackinfo']['Item_Number_3']] = Rackdict['rackinfo']['color3']
    if Rackdict['rackinfo']['Item_Number_4'] != ' ':
        colormap[Rackdict['rackinfo']['Item_Number_4']] = Rackdict['rackinfo']['color4']
    if Rackdict['rackinfo']['Item_Number_5'] != ' ':
        colormap[Rackdict['rackinfo']['Item_Number_5']] = Rackdict['rackinfo']['color5']


    list = colormap.keys()
    if len(list) == 0:
        print('TOM ITEMNR')

    for key in colormap.keys():



        serialDB.conn.layout = 'ODP_Item_Register'
        serialDB.conn.login()

        findquery_item = [
            {"ItemNumber": f"=={key}"}
        ]
        try:
            foundset3 = serialDB.conn.find(findquery_item, limit=1)
        except Exception as e:
            print('error er ', e)
            serialDB.conn.logout()
            return json.dumps({'message': 'Could not fetch iteminfo'}), 401
        serialDB.conn.logout()


        valuedict = dict()
        valuedict['color'] = colormap[key]
        itemdict = dict()

        if foundset3[0].to_dict(ignore_portals=True)['TubeOD'] != 'N/A':
            itemdict['TubeOD'] = foundset3[0].to_dict(ignore_portals=True)['TubeOD']

        if foundset3[0].to_dict(ignore_portals=True)['Weight'] != 'N/A':
            itemdict['Weight'] = foundset3[0].to_dict(ignore_portals=True)['Weight']

        if foundset3[0].to_dict(ignore_portals=True)['Grade'] != 'N/A':
            itemdict['Grade'] = foundset3[0].to_dict(ignore_portals=True)['Grade']

        if foundset3[0].to_dict(ignore_portals=True)['Wall_Thickness'] != 'N/A':
            itemdict['Wall Thickness'] = foundset3[0].to_dict(ignore_portals=True)['Wall_Thickness']

        if foundset3[0].to_dict(ignore_portals=True)['Tool_Joint_ID'] != 'N/A':
            itemdict['Tool Joint ID'] = foundset3[0].to_dict(ignore_portals=True)['Tool_Joint_ID']

        if foundset3[0].to_dict(ignore_portals=True)['Tool_Joint_OD'] != 'N/A':
            itemdict['Tool Joint OD'] = foundset3[0].to_dict(ignore_portals=True)['Tool_Joint_OD']

        if foundset3[0].to_dict(ignore_portals=True)['Equipment'] != 'N/A':
            itemdict['Equipment'] = foundset3[0].to_dict(ignore_portals=True)['Equipment']

        if foundset3[0].to_dict(ignore_portals=True)['Range'] != 'N/A':
            itemdict['Range'] = foundset3[0].to_dict(ignore_portals=True)['Range']

        valuedict['iteminfo'] = itemdict
        colormap[key] = valuedict


    Rackdict['colormap'] = colormap
    print(colormap)

    return Rackdict




























