---
title: "Cancel virtual server"
description: "Example of how to cancel a virtual server (VSI) through a DELETE API operation"
date: "2015-02-15"
classes: ["SoftLayer_Virtual_Guest"]
tags:
  - "vsi"
  - "delete"
---

Operation: `DELETE`

URL: `SoftLayer_Virtual_Guest/{server_id}`

Example CURL: `curl --user userid:api_key curl -X DELETE
https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/123456`


Example Response:
```
true
```
