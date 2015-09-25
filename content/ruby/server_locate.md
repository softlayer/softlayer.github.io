---
title: "Server Locate"
description: "List specific location for virtual machines"
date: "2014-09-30"
classes: ["SoftLayer_Account"]
tags:
    - "virtual"
    - "datacenter"
    - "objectMask"
    - "objectFilter"
---


```ruby
require 'softlayer_api'
require 'table_print'

softlayer_client = SoftLayer::Client.new()
account = SoftLayer::Account.account_for_client(softlayer_client)

servers = SoftLayer::VirtualServer.find_servers(:client => softlayer_client, :object_mask => 'mask[location.pathString]')
location_info = servers.map do |server|
  datacenter, server_room, rack, slot = server['location']['pathString'].split('.')
  { :server => server.fullyQualifiedDomainName,
    :data_center => datacenter, 
    :server_room => server_room, 
    :rack => rack, 
    :slot => slot
  }
end


tp location_info
```
