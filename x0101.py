# -*- coding:utf-8 -*-
import struct

clusetrId_Onoff = 0x0006
clusetrId_Level = 0x0008

def deviceId():
    return 1

def attributeReportList():
    return [
        (
            clusetrId_Level,
            [{
                "attributeId" : 0x0000,
                "attributeType" : "ZCL_DATATYPE_UINT8",
                "minReportInterval" : 1,
                "maxReportInterval" : 60,
                "reportableChange" : 1
            }]
        ),
        (
            clusetrId_Onoff,
            [{
                "attributeId" : 0x0000,
                "attributeType" : "ZCL_DATATYPE_BOOLEAN",
                "minReportInterval" : 1,
                "maxReportInterval" : 60,
                "reportableChange" : 1
            }]
        )
    ]
    
def Desc(endpointId):
    return {
        "ep":endpointId,
        "devid":2,
        "cmdlist":[0,1,2],
        "attrlist":[
            {"id":0,"value":1},
            {"id":1,"value":1}
        ]
    }
    
def newAttribute_Convert(clusterId, attributeRecordList):  
    if clusterId == clusetrId_Onoff:
        attrid = 1
    else:
        attrid = 0
    attributeList = []
    for attributeRecord in attributeRecordList:
        if attributeRecord["attributeId"] == 0x0000:
            if attrid == 1:
                if attributeRecord["attributeValue"] > 0:
                    attributeRecord["attributeValue"] = 0
                else:
                    attributeRecord["attributeValue"] = 1
            else:
                attributeRecord["attributeValue"] = attributeRecord["attributeValue"] * 100 / 255
            attributeList.append({
                "id":attrid,
                "value":attributeRecord["attributeValue"]})
    return attributeList

def readAttribute_Convert(attributeIds):
    record = []
    for attrid in attributeIds:
        if attrid == 0:
            record.append((clusetrId_Level,[0]))
        elif attrid == 1:
            record.append((clusetrId_Onoff,[0]))
    return record

def sendCommand_Convert(cmdId, op):
    if cmdId == 0:
        return clusetrId_Onoff, 1, ""
    elif cmdId == 1:
        return clusetrId_Onoff, 0, ""
    elif cmdId == 2:
        op, = struct.unpack("B", op[0])
        op = op * 255 / 100
        if op > 255:
            op = 255
        return clusetrId_Level, 4, struct.pack("BBB", op, 5, 0)
    
    
    
    