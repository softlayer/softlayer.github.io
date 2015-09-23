---
title: "List Packages"
description: "A handy script with a few examples on how to interact with packages"
date: "2015-08-28"
classes: ["SoftLayer_Product_Package","SoftLayer_Location_Group_Pricing"]
tags:
    - "ordering"
    - "categories"
    - "packages"
    - "locations"
---

```python

import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()
      
    def main(self):
        """
        Gets ALL packages, and prints their name and price descriptions
        """
        mask = "mask[hourlyBillingAvailableFlag]"
        result = self.client['Product_Package'].getAllObjects();
        for product in result:
            print str(product['id']) + " - " + product['name']
        for prices in result['itemPrices']:
            print str(prices['id']) + " - " + prices['item']['description']

        # result has a LOT of stuff in it, only print it out if you are ready
        # pp.pprint(result)

    def getPackage(self, package_id=0):
        """
        Gets a specific package and prints out some useful information
        """
        mask = "mask[items[prices]]"

        # Not all packages are available in all locations, you can check that with getLocations()
        # locations = self.client['Product_Package'].getLocations(id=package_id)
        # pp(locations)

        result = self.client['Product_Package'].getObject(mask=mask,id=package_id)
        # result has a LOT of output
        # pp(result)
        for item in result['items']:
            print str(item['id']) + " - " + item['description'] + " --- " + item['keyName']
            for prices in item['prices']:
                print "\t" + str(prices['id']) + " - locationGroupId: " + str(prices['locationGroupId']) 

        # Will only get the server items for this package
        # serverItems = self.client['Product_Package'].getActiveServerItems(id=package_id)
        # print "SERVER ITEMS"
        # pp(serverItems)

        # Will only get the RAM items for the package
        # ramItems = self.client['Product_Package'].getActiveRamItems(id=package_id)
        # print "RAM ITEMS"
        # pp(ramItems)

     
    
    def getAllLocations(self):
        mask = "mask[id,locations[id,name]]"
        result = self.client['SoftLayer_Location_Group_Pricing'].getAllObjects(mask=mask);
        pp(result)

if __name__ == "__main__":
    main = example()
    main.main()
    main.getPackage(126)
    main.getAllLocations()  

```
