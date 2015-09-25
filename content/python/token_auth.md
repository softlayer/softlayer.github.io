---
title: "Token Authentication"
description: "Authenticate to the API with a username + password instead of an API key. Might be useful if you want to GET the api key without logging in to the portal"
date: "2015-06-09"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "TokenAuthentication"
---

```python
import SoftLayer
from SoftLayer import auth as slauth
import pprint

class tokenAuth():

    def main(self):
        client = SoftLayer.Client()
        result = client['User_Customer'].getPortalLoginToken(
            'username',
            'password!',
            None,
            None)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(result)
        authInfo =  slauth.TokenAuthentication(result['userId'], result['hash'])
        print("Authentication:")
        pp.pprint(authInfo)
        client = SoftLayer.Client(auth=authInfo)
        apiKey = client['SoftLayer_User_Customer'].getApiAuthenticationKeys(
            id=result['userId'])
        pp.pprint(apiKey)


if __name__ == "__main__":
    main = tokenAuth()
    main.main()
```
