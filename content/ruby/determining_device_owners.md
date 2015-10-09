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
require 'pp'

user = "set me"
api_key  = "set me"

billing = SoftLayer::Service.new("SoftLayer_Account",:username => user,:api_key => api_key)

object_mask = "mask[fullyQualifiedDomainName,billingItem[categoryCode,description,createDate,orderItem[order[userRecord[username]]]]]"

hardware_list = billing.object_mask(object_mask).getHardware
virtual_guest_list = billing.object_mask(object_mask).getVirtualGuests

def describe(item)
  domain_name = nil; category_code = nil; description = nil; create_date = nil; user_name = nil;
  begin
    domain_name = item["fullyQualifiedDomainName"]
    category_code = item["billingItem"]["categoryCode"]
    description = item["billingItem"]["description"]
    create_date = item["billingItem"]["createDate"]
    user_name = item["billingItem"]["orderItem"]["order"]["userRecord"]["username"]
  rescue => ex
    puts ex.message
  end
  return "'" + (domain_name ? domain_name  : " no fullyQualifiedDomainName " ) + "'" +
         " category code: " + "'" + (category_code ? category_code  : " no categoryCode " ) + "'" +
         " description: " + "'" + (description ? description  : " no description " ) + "'" +
         " was created by " + "'" + (user_name ? user_name  : " no username " ) + "'" +
         " on " + "'" + (create_date ? create_date  : " no createDate " ) + "'"
end

for item in hardware_list do
  puts "Hardware " + describe(item)
end

for item in virtual_guest_list do
  puts "Virtual Guest " + describe(item)
end

```
