---
title: "Server Bandwidth"
description: "A handy script to get and print relevant server bandwidth details"
date: "2015-06-15"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "server"
    - "bandwidth"
---

```python
import SoftLayer
import pprint

class example():

    def __init__(self):
        user = ''
        key = ''
        self.client = SoftLayer.Client(username = user, api_key = key)

    def main(self):
        pp = pprint.PrettyPrinter(indent=2)
        theMask = "mask[inboundPrivateBandwidthUsage,inboundPublicBandwidthUsage,outboundPrivateBandwidthUsage,outboundPublicBandwidthUsage]"
        result = self.client['SoftLayer_Account'].getHardware()
        print "server_name,public_in,public_out,private_in,private_out"
        
        for server in result:
            #getHardware() only returns SoftLayer_Hardware, which doesn't have the private bw usage metrics, for some reason.
            # So we just use SoftLayer_Hardware_Server here, which has more detailed information
            serverInfo = self.client['SoftLayer_Hardware_Server'].getObject(id=server['id'],mask=theMask)

            # use .get() to avoid exceptions
            pubin = serverInfo.get('inboundPublicBandwidthUsage', '--')
            pubout = serverInfo.get('outboundPublicBandwidthUsage', '--')
            privin =serverInfo.get('inboundPrivateBandwidthUsage', '--')
            privout = serverInfo.get('outboundPrivateBandwidthUsage', '--')

            print(serverInfo['fullyQualifiedDomainName'] + ","),
            print(pubin + ","),
            print(pubout + ","),
            print(privin + ","),
            print(privout)


if __name__ == "__main__":
    main = example()
    main.main()
```