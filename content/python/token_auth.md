---
title: "Password Auth"
description: "Authenticate to the API with a username + password instead of an API key. Might be useful if you want to GET the api key without logging in to the portal"
date: "2015-06-09"
classes: 
    - "SoftLayer_Account"
tags:
    - "authentication"
---

```python
import SoftLayer
client = SoftLayer.Client()
client.authenticate_with_password("username", "password")
print client.call('Account', 'getCurrentUser', mask='id,apiAuthenticationKeys')
```
