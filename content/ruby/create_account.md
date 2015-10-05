---
title: "Create child SoftLayer Account"
description: "Create SoftLayer End-Customer Account on Brand Account"
date: "2014-09-01"
classes: ["SoftLayer_Brand"]
tags:
  - "bap"
---

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new

account_service = client['Account']
brand_service = client['Brand']

brand = account_service.getBrand

cust_account = {
  brandId: brand['id'].to_i, # change me
  allowedPptpVpnQuantity: 1,
  claimedTaxExemptTxFlag: false,
  companyName: '', # change me
  isReseller: 0,
  lateFeeProtectionFlag: true,
  firstName: '', # change me
  lastName: '', # change me
  email: '', # change me
  officePhone: '', # change me
  address1: '', # change me
  city: '', # change me
  state: '', # change me
  postalCode: '', # change me
  country: '' # change me
}

puts ''
pp cust_account
puts ''

begin
  result = brand_service.createCustomerAccount(cust_account)
  puts 'Result: '
  pp result
rescue Exception => e
  puts "Error: #{e}"
end
```

