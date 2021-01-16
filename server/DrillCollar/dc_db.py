from flask import json
from Filemaker.connection import Filemaker


dcDB = Filemaker('ODP_Drill_Collar_Summery')



def db_getdcPDF(orderno):
    dcDB.conn.layout = 'ODP_Drill_Collar_Summery'
    try:
        dcDB.conn.login()
        res = dcDB.conn.perform_script('dc1', orderno)
    except Exception as e:
        print('Error: ', e)
        dcDB.conn.logout()
    else:
        if res[1]:
            print(res)
            return ({
                'error': res[1]
            })
        else:
            findquery = [
                {"Order_No": f"=={orderno}"}
            ]
            sortby = [
                {"fieldName": "Order_No", "sortOrder": "ascend"}
            ]
            try:
                foundset = dcDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                dcDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dc pdf, error: {e}"}),401
            dcDB.conn.logout()
            return ({
                'pdflink': foundset[0].to_dict()['subbe']
            })

def db_getdc(username):
    dcDB.conn.layout = 'ODP_Drill_Collar_Summery'
    dcDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "descend"}
    ]
    try:
        foundset = dcDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        dcDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"}), 401
    dcDB.conn.logout()
    liste = []
    for record in foundset:
        record_dict = {
            'Order_No': record.to_dict()['Order_No'],
            'Returned_From': record.to_dict()['Returned_From'],
            'Returned_Date': record.to_dict()['Inspection_Date'],
            'Ref': record.to_dict()['Ref'],
            'Item_No': record.to_dict()['Item_No'],
            'Equipment': record.to_dict()['Equipment'],
            'Weight': record.to_dict()['Weight'],
            'Grade': record.to_dict()['Grade'],
            'Connection': record.to_dict()['Connection_Rec'],
            'Inspection_Spec': record.to_dict()['Inspection_Spec']
        }
        liste.append(record_dict)
    return liste