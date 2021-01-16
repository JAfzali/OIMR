from flask import json
from Filemaker.connection import Filemaker


dpDB = Filemaker('ODP_DP_Summery_Copy')



def db_getdpPDF(orderno):
    dpDB.conn.layout = 'ODP_DP_Summery_Copy'
    try:
        dpDB.conn.login()
        res = dpDB.conn.perform_script('reqdp', orderno)
    except Exception as e:
        print('Error: ', e)
        dpDB.conn.logout()
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
                foundset = dpDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                dpDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp pdf, error: {e}"})
            dpDB.conn.logout()
            return ({
                'pdflink': foundset[0].to_dict()['container']
            })

def db_getdp(username):
    dpDB.conn.layout = 'ODP_DP_Summery_Copy'
    dpDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "descend"}
    ]
    try:
        foundset = dpDB.conn.find(findquery, sortby, limit=500)
    except Exception as e:
        print('Error: ', e)
        dpDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"})
        dpDB.conn.logout()
    liste = []
    for record in foundset:
        record_dict = {
            'Order_No': record.to_dict()['Order_No'],
            'Returned_From': record.to_dict()['Returned_From'],
            'Returned_Date': record.to_dict()['Returned_Date'],
            'Ref': record.to_dict()['Ref'],
            'Item_No': record.to_dict()['Item_No'],
            'Weight': record.to_dict()['Weight'],
            'Grade': record.to_dict()['Grade'],
            'Connection': record.to_dict()['Connection'],
            'Spec': record.to_dict()['Spec']
        }
        liste.append(record_dict)
    return liste

def db_getdpExcel(orderno):
    dpDB.conn.layout = 'ODP_DP_Summery_Copy'
    try:
        dpDB.conn.login()
        res = dpDB.conn.perform_script('excel1', orderno)
    except Exception as e:
        print('Error: ', e)
        dpDB.conn.logout()
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
                foundset = dpDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                dpDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            dpDB.conn.logout()
            link = foundset[0].to_dict()['excel'].replace("?", ".xlsx?")
            print(link)
            return ({
                'excellink': link
            })


