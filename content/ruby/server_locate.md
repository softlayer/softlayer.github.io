---
title: "Server Locate"
description: "List specific physical location for virtual machines"
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

SoftLayer::Client.default_client = SoftLayer::Client.new

servers = SoftLayer::VirtualServer.find_servers(object_mask: 'mask[location.pathString]')
location_info = servers.map do |server|
  datacenter, server_room, rack, slot = server['location']['pathString'].split('.')
  {
    server: server.fullyQualifiedDomainName,
    data_center: datacenter,
    server_room: server_room,
    rack: rack,
    slot: slot
  }
end


tp location_info
```
