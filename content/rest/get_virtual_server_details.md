---
title: "Get virtual server details"
description: "Example of how to retrieve the details of a virtual server through a GET API operation. The list of fields returned can be customized by adding or removing fields from the objectMask"
date: "2015-02-15"
classes: ["SoftLayer_Virtual_Guest"]
tags:
  - "vsi"
---

Operation: `GET`

URL: `SoftLayer_Virtual_Guest/{server_id}`

Example CURL: `curl --user userid:api_key
"https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/
7743084.json?objectMask=domain;fullyQualifiedDomainName;hostname;id;primaryBack
endIpAddress;primaryIpAddress;status.keyName"`


Example Response:
```json
{
    "domain":"lab01.softlayer.ws",
    "fullyQualifiedDomainName":"test03.lab01.softlayer.ws",
    "hostname":"test03",
    "id":7743084,
    "primaryBackendIpAddress":"10.118.68.8",
    "primaryIpAddress":"168.1.79.8",
    "status":{
        "keyName":"ACTIVE",
        "name":"Active"
    }
}
```
