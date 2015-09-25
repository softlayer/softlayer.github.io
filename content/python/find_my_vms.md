---
title: "Find active VMs by creator"
description: "Retrieves the list of virtual instances (VSIs) by the person who created them. If no parameter is provided the code uses the ID you are logged into the SL CLI with."
date: "2015-06-23"
classes:
  - "SoftLayer_Account"
  - "SoftLayer_VirtualGuest"
tags:
  - "vsis"
  - "creator"
---

```python
'''
Code example of how to list virtual instances from a SoftLayer account
You can call the script from the command and provide the user ID you
want to check. The script expects that you have the SoftLayer CLI
installed and have it configured with the credentials you'd like
to use with SoftLayer.

You can run the script with the user ID you'd like to check under
the account you have configured:
find_my_active_vms userid

The output of the script is in a csv format with tabs as the
column separator.
'''
from __future__ import print_function
import sys
import SoftLayer


def list_my_vms(creator_id=None):
    """
    Get the list of active VMs based on the creator ID

    Keyword arguments:
    creator_id -- the SoftLayer ID of the VM's creator (default: None)
    """

    # create a client to the SoftLayer_Account API service.
    client = SoftLayer.Client()

    # number of results that we expect at a time
    chunk = 200
    mask = "id,fullyQualifiedDomainName,primaryIpAddress,createDate,billingItem[orderItem[description, order[userRecord[username], id]]]"

    # get the data from the SoftLayer APIs
    vms = client.iter_call("Account", "getVirtualGuests", chunk=chunk, mask=mask)
    if creator_id is None:
        # if the creator wasn't provided use the
        # user provided to the API call as the creator
        creator_id = client.auth.username

    # add table header
    print('VM ID', '\t', 'Host', '\t', 'Public IP', '\t', 'Create Date')
    for vsi in vms:
        # navigate to the creator property under the VMs billing item
        if 'billingItem' in vsi.keys():
            billing_item = vsi['billingItem']
            if 'orderItem' in billing_item.keys():
                vm_creator_userid = billing_item['orderItem']['order']['userRecord']['username']
                if creator_id == vm_creator_userid:
                    print(str(vsi['id']), '\t',
                          vsi['fullyQualifiedDomainName'], '\t',
                          vsi.get('primaryIpAddress', 'N/A'), '\t', vsi['createDate'])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        list_my_vms()
    else:
        list_my_vms(sys.argv[1])

```
