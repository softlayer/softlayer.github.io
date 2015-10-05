---
title: "Set user permissions"
description: "Adds the TICKET_ADD permission to a user"
date: "2015-10-4"
classes:
    - "SoftLayer_User_Customer"
tags:
    - "permissions"
    - "users"

---

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the SoftLayer API are grabbed from the config file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new
user_service = client['User_Customer']

# List the user permissions
USER_ID = 172536 # Change me. User id of user to inspect.
pp user_service.object_with_id(USER_ID).getPermissions

# add permission
new_permission = { keyName: 'TICKET_ADD' }
result = user_service.object_with_id(USER_ID).addPortalPermission(new_permission)
unless result
  puts 'Failed to add permission'
  exit 1
end

# list user permissions again
pp user_service.object_with_id(USER_ID).getPermissions
```
