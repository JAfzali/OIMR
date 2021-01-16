import os
import fmrest
import os
os.environ['fmrest_timeout'] = '20'






class Filemaker:
    def __init__(self,layout):
        self.conn  = fmrest.Server('https://a822757.fmphost.com',
                    user='subbe',
                    password='subbe2019',
                    database='Main_Menu',
                    auto_relogin=True,
                    layout=layout,
                   )
        os.environ['fmrest_timeout'] = '20'
    def searchtest(self):
        find = [
            {"Customer": "=Ocean IMR AS","omit" : "true"}
        ]
        sortby = [
            {"fieldName": "Customer","sortOrder": "ascend"}
        ]
        foundset = self.conn.find(find, sort=sortby,limit=10)
        for record in foundset:
            print(foundset.info)

    def getUserName(self,email):
        findquery = find = [
            {"Customer_Email": f"=={email}"}
        ]
        sortby = [
            {"fieldName": "Customer_Email", "sortOrder": "ascend"}
        ]
        foundset = self.conn.find(findquery,sortby,limit=1)
        return foundset[0].Customer








