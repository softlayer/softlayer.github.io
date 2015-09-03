---
title: "Get IPMI info for BMS"
description: "lorem ipsum"
date: "2014-09-01"
categories:
  - "SoftLayer_Account"
tags:
  - "IPMI"
  - "dedicated"
---

```
import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging
 
 apiUsername = ''
 apiKey = ''
  
	 
	 pp = pprint.PrettyPrinter(indent=4)
	 client = SoftLayer.Client(username=apiUsername,api_key=apiKey)
	  
		mask =
		"mask[networkManagementIpAddress,remoteManagementAccounts[username,password]]"
		 
		 result = client['SoftLayer_Account'].getHardware(
```
