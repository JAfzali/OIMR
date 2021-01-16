from flask import request,Blueprint,jsonify,Response,json
from KCAD import kcad_db as kdb

kcad = Blueprint('kcad', __name__)

@kcad.route('/dpjson',methods=['GET'])
def dpjson():
    info = kdb.getDrillPipeData()

    return Response(str(json.dumps(info, indent=4, sort_keys=True)),
                    mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=drillpipe.json'})

@kcad.route('/hwjson',methods=['GET'])
def hwjson():
    info = kdb.getHeavyWeightData()

    return Response(str(json.dumps(info, indent=4, sort_keys=True)),
                    mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=heavyweight.json'})

@kcad.route('/dcjson',methods=['GET'])
def dcjson():
    info = kdb.getDrillCollarData()

    return Response(str(json.dumps(info, indent=4, sort_keys=True)),
                    mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=drillcollar.json'})

@kcad.route('/test',methods=['GET'])
def test():
    return kdb.getDrillPipeData()


