---
title: "Create virtual server"
description: "Example of how to create a new virtual server (VSI) through a POST API operation"
date: "2015-02-15"
classes: ["SoftLayer_Virtual_Guest"]
tags:
  - "vsi"
  - "create"
---

Operation: `POST`

URL: `SoftLayer_Virtual_Guest.json?objectMask=id`

Example CURL: `curl -X POST --data @vs_create.json --user userid:api_key
https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest.json?objectMask=id`


Input JSON:
```json
{
    "parameters" : [
        {
            "hostname" : "myhostname",
            "domain" : "my.domain.com",
            "startCpus" : 1,
            "maxMemory" : 1024,
            "datacenter" : {
                "name" : "wdc01"
                },
            "hourlyBillingFlag" : true,
            "localDiskFlag" : true,
            "operatingSystemReferenceCode": "UBUNTU_LATEST"
        }
    ]
}
```

Example Response:
```json
{"id":7742740}
```
