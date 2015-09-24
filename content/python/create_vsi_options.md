---
title: "Create a new virtual server with all options"
description: "Creates a new virtual server (VSI) and demonstrates the many options that can be used to customize the creation. The code includes a commented out section that will create a price quote for the order instead of actually placing the virtual server order."
date: "2015-08-01"
classes:
  - "SoftLayer_VirtualGuest"
tags:
  - "vsis"
  - "create"
---

```python
'''
An example of how to create a VSI from the SL python library
'''
from __future__ import print_function
import SoftLayer
from SoftLayer.managers.vs import VSManager

def create_vsi():
    #Create a client to the SoftLayer_Account API service.
    #Note: currently set without the user ID and API key since
    #it will by default use the values set in the CLI
    #to use other values use SoftLayer.Client(sl_username, sl_api_key)
    client = SoftLayer.Client()
    vsi_mgr = VSManager(client)

    # uncomment to display create options
    # print(vsi_mgr.get_create_options())

    # common values
    datacenter = 'sjc01' # the data center code
    domain = 'example.com' # the domain name suffix for the host
    os_code = 'CENTOS_6_64' # the operating system code
    local_disk = True # local disk or SAN
    hourly = True # hourly or monthly billing
    dedicated = False # multi-tenant or single tenant
    private_vlan = '825831' # VLAN for the server see VLAN list above
    nic_speed = 1000 # speed of network device
    disks = [100] # size of the disks
    private = True # private networking only or include public internet networking as well
    ssh_keys = [227113, 229467] # the IDs of the ssh keys to load on the server - use slcli sshkey list

    # server properties
    hostname = 'myhost'
    cpus = 4
    memory = 8192
    tags = 'owner:bob,project:poc,type:docker'

    # code that can verify the create operation without actually doing it
    # template = vsi_mgr.verify_create_instance(hostname=hostname, domain=domain,
    #                                 cpus=cpus, memory=memory, datacenter=datacenter,
    #                                 os_code=os_code, local_disk=local_disk,
    #                                 hourly=hourly, dedicated=dedicated,
    #                                 private_vlan=private_vlan, disks=disks,
    #                                 nic_speed=nic_speed, private=private,
    #                                 ssh_keys=ssh_keys, tags=tags)
    # print(template)

    result = vsi_mgr.create_instance(hostname=hostname, domain=domain,
                                     cpus=cpus, memory=memory, datacenter=datacenter,
                                     os_code=os_code, local_disk=local_disk,
                                     hourly=hourly, dedicated=dedicated,
                                     private_vlan=private_vlan, disks=disks,
                                     nic_speed=nic_speed, private=private,
                                     ssh_keys=ssh_keys, tags=tags)
    print(result)

if __name__ == '__main__':
    create_vsi()

```
