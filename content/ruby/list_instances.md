---
title: "List Instances"
description: "Shows how to use the ruby client's VirtualServer class"
date: "2015-10-06"
tags:
    - "VirtualServer"
---

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
SoftLayer::Client.default_client = SoftLayer::Client.new

pp SoftLayer::VirtualServers.find_servers
```