---
title: "Set a server's metadata"
description: "Set a server's metadata"
date: "2015-03-23"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "server"
    - "metadata"
---

```python
import SoftLayer
import pprint

server = 132672 

api_username = ''
api_key = ''
pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=api_username,api_key=api_key)

mask = "mask[attributes]"

# Sets the metadata for this server to tttttt
result1 = client['SoftLayer_Hardware_Server'].setUserMetadata({'value': 'tttttt'},id=server)
pp.pprint(result1)

result2 = client['SoftLayer_Hardware_Server'].getObject(mask=mask,id=server)

pp.pprint(result2)
```
