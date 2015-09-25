---
title: "Get Hardware hostnames"
description: "Calls SoftLayer_Account::getObect() to retrieve some basic information about an account, and uses an objectMask to retrieve the hostname of all hardware on the account"
date: "2015-09-30"
classes: 
    - "SoftLayer_Account"
tags:
    - "objectMask"
---
Operation: `GET`

Method: [`SoftLayer_Account::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Account/getObject)

URL: `SoftLayer_Account/getObject?objectMask=mask\[companyName,hardware\[hostname\]\]"`

Example CURL: `curl -u username:api_key "https://api.softlayer.com/rest/v3/SoftLayer_Account/getObject?objectMask=mask\[companyName,hardware\[hostname\]\]"`

Example Response:
```json
{
    "companyName": "SoftLayer Internal - Development Community",
    "hardware": [
        {
            "hostname": "bsdal5167180245106688"
        },
        {
            "hostname": "db-server"
        },
        {
            "hostname": "db-server"
        },
        {
            "hostname": "deleteme"
        }
    ]
}
```

