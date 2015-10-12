---
title: "Determining SoftLayer Device Owners"
description: "Determining which user on an account ordered a device"
date: "2015-10-09"
classes: ["SoftLayer_Account"]
tags:
    - "customer"
    - "objectMask"
    - "objectFilter"
---

```ruby
require 'softlayer_api'
require 'vine'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new

billing = client['Account']

object_mask = 'mask[fullyQualifiedDomainName,billingItem[categoryCode,description,createDate,orderItem[order[userRecord[username]]]]]'

hardware_list = billing.object_mask(object_mask).getHardware
virtual_guest_list = billing.object_mask(object_mask).getVirtualGuests

def describe(item)
  domain_name = item.access('fullyQualifiedDomainName') || 'no fullyQualifiedDomainName'
  category_code = item.access('billingItem.categoryCode') || 'no categoryCode'
  description = item.access('billingItem.description') || 'no description'
  create_date = item.access('billingItem.createDate') || 'no createDate'
  user_name = item.access('billingItem.orderItem.order.userRecord.username') || 'no username'

  return "'#{domain_name}', category code: '#{category_code}', "\
         "description: '#{description}', was created by: '#{user_name}' "\
         "on '#{create_date}'"
end

for item in hardware_list do
  puts "Hardware " + describe(item)
end

for item in virtual_guest_list do
  puts "Virtual Guest " + describe(item)
end

```
