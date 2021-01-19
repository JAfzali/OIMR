from flask import json
from Filemaker.connection import Filemaker
import os

orderDB = Filemaker('ODP_Tubular_order_Conformation')

def db_getOrderconfirm(username):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    orderDB.conn.login()
    findquery = [
        {"Customer": f"=={username}"}
    ]
    sortby = [
        {"fieldName": "Return_Date", "sortOrder": "descend"}
    ]
    try:
        foundset = orderDB.conn.find(findquery,sortby,limit=500)
    except Exception as e:
        print('Error: ',e)
        orderDB.conn.logout()
        return json.dumps({"message": f"Could not fetch items, error: {e}"})
    orderDB.conn.logout()
    orderliste = []
    for record in foundset:
        record_dict = {
            'Order_No': record.to_dict()['Order_No'],
            'Returned_From': record.to_dict()['Returned_From'],
            'Return_Date': record.to_dict()['Return_Date'],
            'Ref': record.to_dict()['Ref'],
            'Item_No': record.to_dict()['Item_No'],
            'Equipment': record.to_dict()['Equipment'],
            'Weight': record.to_dict()['Weight'],
            'Grade': record.to_dict()['Grade'],
            'Connection_Rec': record.to_dict()['Connection_Rec'],
            'Inspection_Spec': record.to_dict()['Inspection_Spec'],
            'Scope_Of_Work': record.to_dict()['Scope_Of_Work'],
            'QTY_Recived': record.to_dict()['QTY_Recived'],
            'COC_Hardbanding': record.to_dict()['COC_Hardbanding'],
            'COC_Machining': record.to_dict()['COC_Machining'],
            'Receive_No': record.to_dict()['Receive_No'],
            'Completed': record.to_dict()['Completed'],
            'Check_Inspection': record.to_dict()['Check_Inspection'],
            'Check_Machining': record.to_dict()['Check_Machining'],
            'Check_Hardbanding': record.to_dict()['Check_Hardbanding'],
            'Asset': record.to_dict()['Asset'],
            'sent_hb': record.to_dict()['sent_hb'],
            'sent_mach': record.to_dict()['sent_mach']
        }
        orderliste.append(record_dict)
    return orderliste

def db_getOrderpdf(orderno):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    try:
        orderDB.conn.login()
        res = orderDB.conn.perform_script('requestordrnr', orderno)
    except Exception as e:
        print('Error: ',e)
        orderDB.conn.logout()
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
            os.environ['fmrest_timeout'] = '20'
            try:
                foundset = orderDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                orderDB.conn.logout()
                return json.dumps({"message": f"Could not fetch orderpdf, error: {e}"})
            orderDB.conn.logout()

            return ({
                'pdflink': foundset[0].to_dict()['container']
            })

def db_getMachExcel(orderno):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    try:
        orderDB.conn.login()
        res = orderDB.conn.perform_script('mach1', orderno)
    except Exception as e:
        print('Error: ', e)
        orderDB.conn.logout()
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
                foundset = orderDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                orderDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            orderDB.conn.logout()
            link = foundset[0].to_dict()['excel_machining'].replace("?", ".xlsx?")
            return ({
                'excellink': link
            })

def db_getHardExcel(orderno):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    try:
        orderDB.conn.login()
        res = orderDB.conn.perform_script('hard1', orderno)
    except Exception as e:
        print('Error: ', e)
        orderDB.conn.logout()
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
                foundset = orderDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                orderDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            orderDB.conn.logout()
            link = foundset[0].to_dict()['excel_hardbanding'].replace("?", ".xlsx?")
            return ({
                'excellink': link
            })

def db_getHardExcelHW(orderno):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    try:
        orderDB.conn.login()
        res = orderDB.conn.perform_script('hardHW1', orderno)
    except Exception as e:
        print('Error: ', e)
        orderDB.conn.logout()
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
                foundset = orderDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                orderDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            orderDB.conn.logout()
            link = foundset[0].to_dict()['excel_hardHW'].replace("?", ".xlsx?")
            return ({
                'excellink': link
            })

def db_getMachExcelHW(orderno):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    try:
        orderDB.conn.login()
        res = orderDB.conn.perform_script('machHW1', orderno)
    except Exception as e:
        print('Error: ', e)
        orderDB.conn.logout()
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
                foundset = orderDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                orderDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            orderDB.conn.logout()
            link = foundset[0].to_dict()['excel_macHW'].replace("?", ".xlsx?")
            return ({
                'excellink': link
            })

def db_getMachExcelDC(orderno):
    orderDB.conn.layout = 'ODP_Tubular_order_Conformation'
    try:
        orderDB.conn.login()
        res = orderDB.conn.perform_script('machDC1', orderno)
    except Exception as e:
        print('Error: ', e)
        orderDB.conn.logout()
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
                foundset = orderDB.conn.find(findquery, sortby, limit=1)
            except Exception as e:
                print('Error: ', e)
                orderDB.conn.logout()
                return json.dumps({"message": f"Could not fetch dp excel, error: {e}"})
            orderDB.conn.logout()
            link = foundset[0].to_dict()['excel_macDC'].replace("?", ".xlsx?")
            return ({
                'excellink': link
            })






