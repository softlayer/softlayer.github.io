---
title: "Get IPMI info for BMS"
description: "Retrieve IPMI address, username, and password for all hardware on the account"
date: "2014-09-01"
classes:
  - "SoftLayer_Account"
tags:
  - "IPMI"
  - "dedicated"
  - "auth"
---

```python
import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging
 
apiUsername = ''
apiKey = ''
  	 
pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)
	  
mask = "mask[networkManagementIpAddress,remoteManagementAccounts[username,password]]"
		 
result = client['SoftLayer_Account'].getHardware(
```
