---
title: "Create a virtual server from an existing image template"
description: "Provide an image template with a virtual machine order instead of an OS code."
date: "2015-10-07"
classes: ["SoftLayer_Product_Order"]
tags: ["virtual server", "ordering", "deprecated"]

---

```ruby
require 'softlayer_api'
require 'pp'

IMAGE_ID = 'foobar' # change me. Image template global ID.

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
SoftLayer::Client.default_client = SoftLayer::Client.new

order_template = {
    hostname: 'test',
    domain: 'example.com', # change me
    datacenter: 'hou02',
    cores: 2, # 2 x 2.0 GHz Cores
    memory: 4, # 4GB RAM
    private_network_only: false,
    dedicated_host_only: false,
    #os_reference_code: CENTOS_6_64, # CentOS 6.latest minimal (64 bit)
    image_template: SoftLayer::ImageTemplate.template_with_global_id(IMAGE_ID),
    use_local_disk: false, # Use a SAN disk
    hourly: true # Charge me for hourly use, rather than monthly.
}

# Set order template in our order instance,
# Otherwise, you can skip using an order template hash, and just
# set values directly in the order instance like `order.cores = 2`.
order = SoftLayer::VirtualServerOrder.new
order_template.keys.each do |k|
    order.send("#{k}=", order_template[k])
end

pp order.verify
# Uncomment to place the order.
# server = order.place_order!
# pp server
```
