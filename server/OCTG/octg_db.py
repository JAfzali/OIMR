from flask import json
from Filemaker.connection import Filemaker


octgDB = Filemaker('ODP_OCTG_Report')



def db_getoctgPDF(orderno):
    octgDB.conn.layout = 'ODP_OCTG_Report'
    try:
        octgDB.conn.login()
        res = octgDB.conn.perform_script('octg1', orderno)
    except Exception as e:
        print('Error: ', e)
        octgDB.conn.logout()
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
                foundset = octgDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                octgDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dc pdf, error: {e}"})
                octgDB.conn.logout()
            return ({
                'pdflink': foundset[0].to_dict()['subbi']
            })

def db_getoctg(username):
    octgDB.conn.layout = 'ODP_OCTG_Report'
    octgDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "descend"}
    ]
    try:
        foundset = octgDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        octgDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"}),401
    octgDB.conn.logout()
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
            'Connection': record.to_dict()['Connection_1'],
            'Spec': record.to_dict()['Spec']
        }
        liste.append(record_dict)
    return liste