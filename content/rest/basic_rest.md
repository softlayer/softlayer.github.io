---
title: "Basic Rest Examples"
description: "A collection of some of the ways to interact with the REST service"
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
{"companyName":"SoftLayer Internal - Development Community","hardware":[{"hostname":"bsdal5167180245106688"},{"hostname":"db-server"},{"hostname":"db-server"},{"hostname":"deleteme"},{"hostname":"pjacksontestorder"},{"hostname":"rcdeleteme"},{"hostname":"rcpartitionexem"},{"hostname":"rctdeletepar"},{"hostname":"rctestpar2"},{"hostname":"rctestpower"},{"hostname":"rcvtest-6"},{"hostname":"rcvyatta1"}]}
```

