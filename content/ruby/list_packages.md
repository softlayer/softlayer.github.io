---
title: "List Packages"
description: "A handy script with a few examples on how to interact with packages"
date: "2015-10-12"
classes: ["SoftLayer_Product_Package","SoftLayer_Location_Group_Pricing"]
tags:
    - "ordering"
    - "categories"
    - "packages"
    - "locations"
---

```ruby
require 'softlayer_api'
require 'pp'

# Helper function to fetch through all results from SoftLayer api
# using small page sizes and sleeping before every new page fetch.
def fetch_all(service, method)
  records = []; offset = 0; limit = 10
  loop do
    results = service.result_limit(offset, limit).send(method)
    records += results
    break if results.size < limit
    offset += limit
    sleep 3
  end
  records
end

# Credentials to the SoftLayer API are grabbed from the config file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new
package_service = client['Product_Package']

# Show all packages
mask = 'mask[id,name,description,itemPrices]'
all_packages = fetch_all(package_service.object_mask(mask), :getAllObjects)

all_packages.each do |package|
  puts "#{package['id']} - #{package['name']}"
  package['itemPrices'].each do |price|
    puts "#{price['id']} - #{price['item']['description']}"
  end
end

PACKAGE_ID = 126
mask = 'mask[id,name,description,items[id,description,keyName,prices[id,locationGroupId]]]'
product_package = package_service.object_mask(mask).object_with_id(PACKAGE_ID).getObject

# Get locations in which package is available
puts 'PACKAGE LOCATIONS'
pp package_service.object_with_id(PACKAGE_ID).getLocations

# Show a specific product's items with prices
product_package['items'].each do |item|
  puts "#{item['id']} - #{item['description']} - #{item['keyName']}"
  item['prices'].each do |price|
    puts "\t#{price['id']} - locationGroupId: #{price['locationGroupId']}"
  end
end

# Will only get the server items for this package
# puts 'SERVER ITEMS'
# pp package_service.object_with_id(PACKAGE_ID).getActiveServerItems

# Will only get the RAM items for the package
# puts 'RAM ITEMS'
# pp package_service.object_with_id(PACKAGE_ID).getActiveRamItems

# Get all locations
mask = 'mask[id,locations[id,name]]'
puts 'ALL LOCATIONS'
pp client['Location_Group_Pricing'].object_mask(mask).getAllObjects
```
