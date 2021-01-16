from flask import json
from Filemaker.connection import Filemaker

deliveryDB = Filemaker('ODP_Tubular_Delivery_Ticket')

def db_getDelivery(username):
    deliveryDB.conn.layout = 'ODP_Tubular_Delivery_Ticket'
    deliveryDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "descend"}
    ]
    try:
        foundset = deliveryDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        deliveryDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"}),401
    deliveryDB.conn.logout()
    liste = []
    for record in foundset:
        record_dict = {
            'DT_No': record.to_dict()['DT_No'],
            'Sent_To': record.to_dict()['Sent_To'],
            'Rig': record.to_dict()['Rig'],
            'Item_No': record.to_dict()['Item_No'],
            'Equipment': record.to_dict()['Equipment'],
            'Weight': record.to_dict()['Weight'],
            'Grade': record.to_dict()['Grade'],
            'DT_Connection': record.to_dict()['DT_Connection'],
            'Quantity': record.to_dict()['Quantity'],
            'Ref': record.to_dict()['Ref'],
            'Wiresling': record.to_dict()['PDF']
        }
        liste.append(record_dict)
    return liste

def db_getDeliveryPDF(dtno):
    deliveryDB.conn.layout = 'ODP_Tubular_Delivery_Ticket'
    try:
        deliveryDB.conn.login()
        res = deliveryDB.conn.perform_script('requestdtPDF', dtno)
    except Exception as e:
        print('Error: ', e)
        deliveryDB.conn.logout()
    else:
        if res[1]:
            print(res)
            return ({
                'error': res[1]
            })
        else:
            findquery = [
                {"DT_No": f"=={dtno}"}
            ]
            sortby = [
                {"fieldName": "DT_No", "sortOrder": "ascend"}
            ]
            try:
                foundset = deliveryDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                deliveryDB.conn.logout()
                return json.dumps({"message": f"Could not fetch deliverypdf, error: {e}"})
                receivedDB.conn.logout()
            return ({
                'pdflink': foundset[0].to_dict()['container']
            })


def db_getDTExcel(dtno):
    deliveryDB.conn.layout = 'ODP_Tubular_Delivery_Ticket'
    try:
        deliveryDB.conn.login()
        res = deliveryDB.conn.perform_script('dt1', dtno)
    except Exception as e:
        print('Error: ', e)
        deliveryDB.conn.logout()
    else:
        if res[1]:
            print(res)
            return ({
                'error': res[1]
            })
        else:
            findquery = [
                {"DT_No": f"=={dtno}"}
            ]
            sortby = [
                {"fieldName": "DT_No", "sortOrder": "ascend"}
            ]
            try:
                foundset = deliveryDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                deliveryDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            deliveryDB.conn.logout()
            link = foundset[0].to_dict()['excel'].replace("?", ".xlsx?")
            return ({
                'excellink': link
            })