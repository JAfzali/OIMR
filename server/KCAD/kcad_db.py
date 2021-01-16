from Filemaker.connection import Filemaker

kcadDB = Filemaker('ODP_HW_Tally')
customer = 'KCA Deutag'


def getHeavyWeightData():
    HWdict = {}
    HWPipelist = []


    kcadDB.conn.layout = 'ODP_HW_Tally'
    kcadDB.conn.login()

    findquery = [
        {"Customer": f"=={customer}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "ascend"}
    ]
    foundset = kcadDB.conn.find(findquery, sortby, limit=1)
    for record in foundset:
        HWdict = record.to_dict()
    for row in HWdict['portal_Portal | HW_List']:
        HWPipelist.append(row.to_dict())

    HWdict['portal_Portal | HW_List'] = HWPipelist
    HWdict['Pipes'] = HWdict.pop('portal_Portal | HW_List')


    return HWdict




def getDrillCollarData():
    DCdict = {}
    DCPipelist = []

    kcadDB.conn.layout = 'ODP_DC_Tally'
    kcadDB.conn.login()

    findquery = [
        {"Customer": f"=={customer}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "ascend"}
    ]
    foundset = kcadDB.conn.find(findquery, sortby, limit=1)
    for record in foundset:
        DCdict = record.to_dict()
    for row in DCdict['portal_Portal | DC_Tally']:
        DCPipelist.append(row.to_dict())

        DCdict['portal_Portal | DC_Tally'] = DCPipelist
        DCdict['Pipes'] = DCdict.pop('portal_Portal | DC_Tally')

    return DCdict

def getDrillPipeData():
    DPPipelist = []
    testlist= []


    kcadDB.conn.layout = 'ODP_DrillPipe_Tally'
    kcadDB.conn.login()

    findquery = [
        {"Customer": f"=={customer}"}
    ]
    sortby = [
        {"fieldName": "Customer", "sortOrder": "ascend"}
    ]
    foundset = kcadDB.conn.find(findquery, sortby, limit=1)
    for record in foundset:
        DPdic = record.to_dict()
        testdic = {
            'WorkOrderNo': record.Order_No,
            'CustomerPO': record.Customer,
            'DateCreated': record.Inspection_Date,
            'Connection': record.Connection,
            'Grade': record.Grade,
            'Item_No': record.Item_No,
            'ListofPipes': []
        }

    for row in DPdic['portal_Portal | DP Tally']:
        DPPipelist.append(row.to_dict())
        testpipedic = {
            'Bent': row['ODP_DP_Tally_Report::B'],
            'BoxResult': row['ODP_DP_Tally_Report::Box'],
            'Box_HB_H': row['ODP_DP_Tally_Report::Box_HB_H'],
            'BoxHardbandingOD': row['ODP_DP_Tally_Report::Box_HB_OD'],
            'Box_HB_Type': row['ODP_DP_Tally_Report::Box_HB_Type'],
            'BoxOD': row['ODP_DP_Tally_Report::Box_OD'],
            'BoxLength': row['ODP_DP_Tally_Report::Box_TL'],
            'BoxTongSpace': row['ODP_DP_Tally_Report::Box_TS'],
            'Remarks': row['ODP_DP_Tally_Report::Comments'],
            'BoxHardbandingCondition': row['ODP_DP_Tally_Report::HB_Box'],
            'PinHardbandingCondition': row['ODP_DP_Tally_Report::HB_Pin'],
            'InternalCondition': row['ODP_DP_Tally_Report::IPC'],
            'PinResult': row['ODP_DP_Tally_Report::Pin'],
            'Pin_HB_H': row['ODP_DP_Tally_Report::Pin_HB_H'],
            'PinHardbandingOD': row['ODP_DP_Tally_Report::Pin_HB_OD'],
            'Pin_HB_Type': row['ODP_DP_Tally_Report::Pin_HB_Type'],
            'Pin_ID': row['ODP_DP_Tally_Report::Pin_ID'],
            'PinOD': row['ODP_DP_Tally_Report::Pin_OD'],
            'PinLength': row['ODP_DP_Tally_Report::Pin_TL'],
            'PinTongSpace': row['ODP_DP_Tally_Report::Pin_TS'],
            'Slotted': row['ODP_DP_Tally_Report::RS'],
            'SerialNo1': row['ODP_DP_Tally_Report::Serial_No'],
            'ToolClass': row['ODP_DP_Tally_Report::TJ'],
            'BodyClass': row['ODP_DP_Tally_Report::TU'],
            'WallThickness': row['ODP_DP_Tally_Report::Wall'],
            'Length': row['ODP_DP_Tally_Report::dp_length']
        }
        testlist.append(testpipedic)



    DPdic['portal_Portal | DP Tally'] = DPPipelist
    DPdic['Pipes'] = DPdic.pop('portal_Portal | DP Tally')
    testdic['ListofPipes'] = testlist

    return testdic
