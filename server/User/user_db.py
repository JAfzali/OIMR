from flask import Blueprint,request
from Filemaker.connection import Filemaker


userDB = Filemaker('ODP_Customer_Register')

userdict = {
    'Archer Rental': 'Archer Rental',
    'Seadrill West Linus': 'Seadrill',
    'Seadrill West Elara': 'Seadrill',
    'Odfjell Well Services': 'Odfjell Well Services',
    'Saipem': 'Saipem'
}


def getUserName(email):
    userDB.conn.login()
    findquery = [
        {"Customer_Email": f"=={email}"}
    ]
    sortby = [
        {"fieldName": "Customer_Email", "sortOrder": "ascend"}
    ]
    foundset = userDB.conn.find(findquery,sortby,limit=1)
    userDB.conn.logout()
    return foundset[0].Customer

def getUserInfo(email):
    assetlist = []
    userDB.conn.login()
    findquery = [
        {"Customer_Email": f"=={email}"}
    ]
    sortby = [
        {"fieldName": "Customer_Email", "sortOrder": "ascend"}
    ]
    foundset = userDB.conn.find(findquery,sortby,limit=1)
    userDB.conn.logout()
    #Check if user has assets:
    for assets in foundset[0].to_dict()['portal_ODP_Customer_Asset']:
        assetlist.append(assets.to_dict()['ODP_Customer_Asset::Asset_name'])
    print(assetlist)
    return assetlist




#getUserInfo('Henrik.Johannesen@seadrill.com')







