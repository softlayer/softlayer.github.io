---
title: "Set user permissions"
description: "Adds the TICKET_ADD permission to a user"
date: "2015-09-16"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "permissions"
    - "users"

---

```python
import SoftLayer
import pprint

class setPermissions():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):

        pp = pprint.PrettyPrinter(indent=4)
        # the user ID we want to change
        template_user_id = 350000

        # This is just so we can see what permissions we have already
        permissions = self.client['User_Customer'].getPermissions(id=template_user_id)
        pp.pprint(permissions)

        # Adds in a new permissions
        setperm = {'keyName': "TICKET_ADD"}
        users = self.client['User_Customer'].addPortalPermission(setperm, id=template_user_id)
        pp.pprint(users)

        # Make sure it actually worked
        permissions = self.client['User_Customer'].getPermissions(id=template_user_id)
        pp.pprint(permissions)

if __name__ == "__main__":
    main = setPermissions()
    main.main()
```
