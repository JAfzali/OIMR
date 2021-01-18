from flask import json
from Filemaker.connection import Filemaker

receivedDB = Filemaker('Tubular_Received_Report')

def db_getReceivedpdf(receivednr):
    receivedDB.conn.layout = 'Tubular_Received_Report'
    try:
        receivedDB.conn.login()
        res = receivedDB.conn.perform_script('requestrecnr', receivednr)
    except Exception as e:
        print('Error: ', e)
        receivedDB.conn.logout()
    else:
        if res[1]:
            print(res)
            return ({
                'error': res[1]
            })
        else:
            findquery = [
                {"Receive_No": f"=={receivednr}"}
            ]
            sortby = [
                {"fieldName": "Receive_No", "sortOrder": "ascend"}
            ]
            try:
                foundset = receivedDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                receivedDB.conn.logout()
                return json.dumps({"message": f"Could not fetch receivedpdf, error: {e}"})
                receivedDB.conn.logout()

            return ({
                'pdflink': foundset[0].to_dict()['container']
            })

def db_getReceived(username):
    receivedDB.conn.layout = 'Tubular_Received_Report'
    receivedDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Returned_Date", "sortOrder": "descend"}
    ]
    try:
        foundset = receivedDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        receivedDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"})
    receivedDB.conn.logout()
    liste = []
    for record in foundset:
        record_dict = {
            'Receive_No': record.to_dict()['Receive_No'],
            'Returned_Date': record.to_dict()['Returned_Date'],
            'Returned_From': record.to_dict()['Returned_From'],
            'Location': record.to_dict()['Location'],
            'Item_No': record.to_dict()['Item_No'],
            'Quantity_Tubular': record.to_dict()['Quantity_Tubular'],
            'Equipment': record.to_dict()['Equipment'],
            'Asset': record.to_dict()['Asset']
        }
        liste.append(record_dict)
    return liste
