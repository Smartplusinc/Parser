# -*- coding:utf-8 -*-
clusetrId_Onoff = 0x0006

def deviceId():
    return 1

def attributeReportList():
    return [
        (clusetrId_Onoff, [{
            "attributeId" : 0x0000,
            "attributeType" : "ZCL_DATATYPE_BOOLEAN",
            "minReportInterval" : 1,
            "maxReportInterval" : 60,
            "reportableChange" : 1
        }])
    ]
    
def Desc(endpointId):
    return {
        "ep":endpointId,
        "devid":1,
        "cmdlist":[0,1],
        "attrlist":[
            {"id":0,"value":1}
        ]
    }
    
def newAttribute_Convert(clusterId, attributeRecordList):
    #gwAttributeRecord_t to new_attribute.body.attr
    attributeList = []
    if clusterId == clusetrId_Onoff:
        for attributeRecord in attributeRecordList:
            if attributeRecord["attributeId"] == 0x0000:
                if attributeRecord["attributeValue"] == 0:
                    value = 1
                else:
                    value = 0;
                attributeList.append({
                    "id":0,
                    "value":value})
    return attributeList

def readAttribute_Convert(attributeIds):
    if 0 in attributeIds:
        return [(clusetrId_Onoff,[0])]
    return []

def sendCommand_Convert(cmdId, op):
    if cmdId == 0:
        return clusetrId_Onoff, 1, ""
    elif cmdId == 1:
        return clusetrId_Onoff, 0, ""
    else:
        return None
