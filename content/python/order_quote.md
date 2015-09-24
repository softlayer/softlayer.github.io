---
title: "Place quote order"
description: "Retrieve an order object from a quote and place an order based on it"
date: "2014-02-12"
classes: ["SoftLayer_User_Customer","SoftLayer_Account"]
tags:
    - "order"
    - "quote"
---


```python
import SoftLayer.API
from pprint import pprint as pp
 
api_username = ''
api_key = ''
quote_id = 1234

client = SoftLayer.Client(
    username=api_username,
    api_key=api_key,
)

def getOrderContainer(quote_id):
    container = client['Billing_Order_Quote'].getRecalculatedOrderContainer( \
        id=quote_id)
    return container['orderContainers'][0]
 
 
container = getOrderContainer(quote_id)
order = {}
order['complexType'] = 'Container_Product_Order_Virtual_Guest'
order['hardware'] = [{'hostname': 'quotetest', 'domain': 'example.com'}]
order['quanity'] = 1
result = client['Billing_Order_Quote'].placeOrder(order, id=quote_id)

pp(result)

```
