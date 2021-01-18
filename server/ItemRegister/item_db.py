from flask import json
from Filemaker.connection import Filemaker

itemDB = Filemaker('ODP_Item_Register')

def db_getInventory(username):
    itemDB.conn.layout = 'ODP_Item_Register'
    itemDB.conn.login()

    findquery = [
        {"Customer": f"=={username}"},
        {"ODP_Stock_list_List::Total_Item": "==", "omit": "true"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "ascend"}
    ]
    portals = [{'name': 'Portal | Inventory Transactions 2', 'offset': 1, 'limit': 1}]
    try:
        foundset = itemDB.conn.find(findquery,sortby,portals=portals,limit=500)
    except Exception as e:
        print('Error: ',e)
        itemDB.conn.logout()
        return json.dumps({"message" : f"Could not fetch items, error: {e}"})
    itemDB.conn.logout()
    itemliste = []
    for record in foundset:
        record_dict = {
            'Item_No' : record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Item_No'],
            'Site': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Site'],
            'Project': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Project'],
            'Rig_Ready': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Rig_Ready'],
            'Booked': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Booked'],
            'Backlog': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Backlog'],
            'Wepco': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Wepco'],
            'Stamas': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Stamas'],
            'Hardbanding': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Hardbanding'],
            'Scrap': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Scrap'],
            'Limited_Service': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Limited_Service'],
            'On_Hold': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::On_Hold'],
            'Other': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Other'],
            'Shipped': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Shipped'],
            'Total_Yard': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Total_Yard'],
            'Customer_Ref': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Customer_Ref'],
            'Total_Item': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Total_Item'],
            'Comments': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Comments'],
            'Inspection': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Inspection'],
            'Norse': record.to_dict()['portal_Portal | Inventory Transactions 2'][0].to_dict()['ODP_Stock_list_List::Norse'],
            'PDF': record.to_dict()['Certificate'],
            'Equipment': record.to_dict()['Equipment'],
            'Asset' : record.to_dict()['Asset'],
        }
        itemliste.append(record_dict)
    return itemliste


