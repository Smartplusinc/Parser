# -*- coding:utf-8 -*-
import struct

clusterId_windowCovering = 0x0102

def deviceId():
    return 0

def attributeReportList():
    return [
        (clusterId_windowCovering, [{
            "attributeId" : 0x0008,
            "attributeType" : "ZCL_DATATYPE_UINT8",
            "minReportInterval" : 1,
            "maxReportInterval" : 60,
            "reportableChange" : 1
        }])
    ]
def Desc(endpointId):
    return {
        "ep":endpointId,
        "devid":0,
        "cmdlist":[0,1,2,3,4,5,6,7,8,9,10],
        "attrlist":[
            {"id":0,"value":0},
            {"id":1,"value":0},
            {"id":2,"value":0},
            {"id":3,"value":0},
            {"id":4,"value":0}
        ]
    }
def newAttribute_Convert(clusterId, attributeRecordList):
    attributeList = []
    if clusterId == clusterId_windowCovering:
        for attributeRecord in attributeRecordList:
            if attributeRecord["attributeId"] > 0xf000:
                attributeList.append({
                    "id":attributeRecord["attributeId"] & 0x000f,
                    "value":attributeRecord["attributeValue"]})
            elif attributeRecord["attributeId"] == 0x0008:
                attributeList.append({
                    "id":0,
                    "value":attributeRecord["attributeValue"]})
            elif attributeRecord["attributeId"] == 0x0000:
                attributeList.append({
                    "id":1,
                    "value":attributeRecord["attributeValue"]})
    return attributeList
def readAttribute_Convert(attributeIds):
    attrIds = []
    for attrid in attributeIds:
        if attrid == 0:
            attrIds.append(0x0008)
        elif attrid == 1:
            attrIds.append(0x0000)
        elif attrid == 2:
            attrIds.append(0xf002)
        elif attrid == 3:
            attrIds.append(0xf003)
        elif attrid == 4:
            attrIds.append(0xf004)
    return [(clusterId_windowCovering, attrIds)]
def sendCommand_Convert(cmdId, op):
    if cmdId < 3:
        return clusterId_windowCovering, cmdId, ""
    elif cmdId == 3:
        return clusterId_windowCovering, 5, op[0]
    else:
        return clusterId_windowCovering, 0x87, struct.pack("B", cmdId) + op
    
    
    
    