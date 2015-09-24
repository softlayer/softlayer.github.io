---
title: "Create an virtual guest"
description: "Creates a new virtual guest with some basic options"
date: "2015-09-30"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "ordering"
    - "postInstallScript"
---

Operation: `POST`

Method: [`SoftLayer_Virtual_Guest::createObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject)

URL: `SoftLayer_Virtual_Guest`

Example CURL: `curl -u username:api_key --data @createVirtualServer.json "https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest"`

Input JSON:
```json
{ 
    "parameters":[ 
    { 
        "datacenter" : {
            "name" : "sjc01"
        },
        "sshKeys" : [
            {"id" : "1234"}
        ],
        "hostname": "new", 
        "domain": "Test.com", 
        "startCpus": 1, 
        "maxMemory": 1024, 
        "hourlyBillingFlag": true, 
        "localDiskFlag": false, 
        "operatingSystemReferenceCode": "DEBIAN_LATEST" ,
        "postInstallScriptUri": "https://pastebin.com/raw.php?i=asf3231"
    } 
    ] 
}

```

Example Response
```json
{
    "accountId":307608,
    "createDate":"2015-09-24T17:42:00-06:00",
    "domain":"Test.com",
    "fullyQualifiedDomainName":"new.Test.com",
    "hostname":"new",
    "id":12742709,
    "lastPowerStateId":null,
    "lastVerifiedDate":null,
    "maxCpu":1,
    "maxCpuUnits":"CORE",
    "maxMemory":1024,
    "metricPollDate":null,
    "modifyDate":null,
    "provisionDate":null,
    "startCpus":1,
    "statusId":1001,
    "uuid":"dfbbf1f8-b53f-4aae-bdfc-1ff61e1a55c5",
    "globalIdentifier":"acea6dac-a135-4620-a9e5-9e429295a92b"
}
```
