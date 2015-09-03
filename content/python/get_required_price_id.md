---
title: "Required price IDs for package"
description: "For any package retrieve a list of options organized by required
category"
date: "2014-09-01"
classes: ["SoftLayer_Product_Package"]
tags:
  - "ordering"
  - "categories"
---
```
import SoftLayer

apiUsername = ''
apiKey = ''
package = 46

client = SoftLayer.Client(username=apiUsername, api_key=apiKey)
categoryObjectMask = "mask[isRequired, itemCategory[id, name]]"

configurations = client['Product_Package'].getConfiguration(
    id=package, mask=categoryObjectMask)

pricesObjectMask = "mask[id;item.description;categories.id]"

prices = client['Product_Package'].getItemPrices(
    id=package, mask=pricesObjectMask)

headerFormat = '%s - %s:'
priceFormat = '    %s -- %s'
for configuration in configurations:
    if (not configuration['isRequired']):
        continue
    print headerFormat % (configuration['itemCategory']['name'],
                          configuration['itemCategory']['id'])
    for price in prices:
        if ('categories' not in price):
            continue
        if any((category.get('id') == configuration['itemCategory']['id']
                for category in price['categories'])):
            print priceFormat % (price['id'], price['item']['description'])
```
