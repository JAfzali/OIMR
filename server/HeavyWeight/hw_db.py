from flask import json,jsonify
from Filemaker.connection import Filemaker



hwDB = Filemaker('ODP_HW_Report')



def db_gethwPDF(orderno):
    hwDB.conn.layout = 'ODP_HW_Report'
    try:
        hwDB.conn.login()
        res = hwDB.conn.perform_script('getHeavyWeightPDF', orderno)
    except Exception as e:
        print('Error: ', e)
        hwDB.conn.logout()
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
                foundset = hwDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                hwDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp pdf, error: {e}"})
            hwDB.conn.logout()
            return ({
                'pdflink': foundset[0].to_dict()['container']
            })

def db_gethw(username):
    hwDB.conn.layout = 'ODP_HW_Report'
    hwDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "descend"}
    ]
    try:
        foundset = hwDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        hwDB.conn.logout()
        return json.dumps({'errors': 'No records found'}), 401
    hwDB.conn.logout()
    liste = []
    for record in foundset:
        record_dict = {
            'Order_No': record.to_dict()['Order_No'],
            'Returned_From': record.to_dict()['Returned_From'],
            'Inspection_Date': record.to_dict()['Inspection_Date'],
            'Ref': record.to_dict()['Ref'],
            'Item_No': record.to_dict()['Item_No'],
            'Equipment': record.to_dict()['Equipment'],
            'Weight': record.to_dict()['Weight'],
            'Grade': record.to_dict()['Grade'],
            'Connection': record.to_dict()['Connection'],
            'Spec': record.to_dict()['Spec']
        }
        liste.append(record_dict)
    return liste

def db_gethwExcel(orderno):
    hwDB.conn.layout = 'ODP_HW_Report'
    try:
        hwDB.conn.login()
        res = hwDB.conn.perform_script('excelhw1', orderno)
    except Exception as e:
        print('Error: ', e)
        hwDB.conn.logout()
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
                foundset = hwDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                hwDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
                hwDB.conn.logout()
            link = foundset[0].to_dict()['excel'].replace("?", ".xlsx?")
            print(link)
            return ({
                'excellink': link
            })
