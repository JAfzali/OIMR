from flask import json
from Filemaker.connection import Filemaker

preinvDB = Filemaker('ODP_Pre_Invoice')

def db_getPreinvPDF(orderno):
    preinvDB.conn.layout = 'ODP_Pre_Invoice'
    try:
        preinvDB.conn.login()
        res = preinvDB.conn.perform_script('requestpreinv', orderno)
    except Exception as e:
        print('Error: ', e)
        preinvDB.conn.logout()
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
                foundset = preinvDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                preinvDB.conn.logout()
                return json.dumps({"message": f"Could not fetch preinvpdf, error: {e}"})
                receivedDB.conn.logout()
            return ({
                'pdflink': foundset[0].to_dict()['container']
            })

def db_getPreinv(username):
    preinvDB.conn.layout = 'ODP_Pre_Invoice'
    preinvDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "descend"}
    ]
    try:
        foundset = preinvDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        preinvDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"})
    preinvDB.conn.logout()
    liste = []
    for record in foundset:
        record_dict = {
            'Order_No': record.to_dict()['Order_No'],
            'Returned_From': record.to_dict()['Returned_From'],
            'Return_Date': record.to_dict()['Return_Date'],
            'Ref': record.to_dict()['Ref'],
            'Item_Number': record.to_dict()['Item_Number'],
            'Equipment': record.to_dict()['Equipment'],
            'Weight': record.to_dict()['Weight'],
            'Grade': record.to_dict()['Grade'],
            'Connection': record.to_dict()['Connection'],
            'Inspection_Specification': record.to_dict()['Inspection_Specification']
        }
        liste.append(record_dict)
    return liste
