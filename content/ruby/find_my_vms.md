---
title: "Find active VMs of specified creator"
description: "Retrieves virtual instances (VSIs) belonging to the specified creator. If no user is specified, it uses the username from the SL Client instance."
date: "2015-10-12"
classes:
  - "SoftLayer_Account"
  - "SoftLayer_VirtualGuest"
tags:
  - "vsis"
  - "creator"
---

```ruby
# Code example of how to list virtual instances from a SoftLayer account.
# You can call the script from the command and provide the username you
# want to filter on. The script expects that you have the SoftLayer gem
# installed and have it configured with the credentials you'd like
# to use with SoftLayer.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44.
#
# You can run the script with the username you'd like to check under
# the account you have configured:
# find_my_active_vms userid
#
# The output of the script is in a csv format with commas as the
# column separator.
require 'softlayer_api'
require 'vine'
require 'csv'

client = SoftLayer::Client.new
account_service = client['Account']
object_mask = 'mask[id,fullyQualifiedDomainName,primaryIpAddress,createDate,billingItem[orderItem[description,order[userRecord[username],id]]]]'

USER_ID = ARGV[0] || client.username

vms = account_service.object_mask(object_mask).getVirtualGuests

csv_string = CSV.generate do |csv|
  csv << ['VM ID', 'Host', 'Public IP', 'Create Date'] # table headers
  vms.each do |vm|
    creator = vm.access('billingItem.orderItem.order.userRecord.username')
    next unless creator == USER_ID
    csv << [vm['id'], vm['fullyQualifiedDomainName'], vm['primaryIpAddress'], vm['createDate']]
  end
end

puts csv_string
```
