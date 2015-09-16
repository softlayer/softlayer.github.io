---
title: "Change Passwords"
description: "Users a prefix to find all matching users on your account, then change their password"
date: "2015-05-30"
classes: ["SoftLayer_User_Customer","SoftLayer_Account"]
tags:
    - "password"
    - "user"
    - "objectFilter"
---


```python

import SoftLayer
import pprint

class example():

    def __init__(self):

        self.client = SoftLayer.Client()
        self.prefix = "PREFIX"
        self.password= "qweASDzxc!23"

    def main(self):
        pp = pprint.PrettyPrinter(indent=4)
        users = self.get_target_users(prefix=self.prefix)
        for user in users:
            print "Changing password for: " + str(user['id']) + " " + user['username']
            result = self.client['User_Customer'].updatePassword(self.password, id=user['id'])
        # pp.pprint(result)

    def get_target_users(self, prefix):
        _filter = {
            'users': {
                'username': {
                    'operation': '*= %s' % (prefix)
                }
            }
        }

        _mask = "mask[id,username]"

        _users = self.client['Account'].getUsers(filter=_filter, mask=_mask)
        return _users

if __name__ == "__main__":
    main = example()
    main.main()

```