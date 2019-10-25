---
title: "Image Template Costs"
description: "A ROUGH estimate for how much all the image templates on your account will cost."
date: "2019-10-25"
classes: 
    - "SoftLayer_Virtual_Storage_Repository"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Network_Component_Firewall"
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
tags:
    - "template"
    - "billing"
---

The way this script works is that first it gets your last invoice, and finds all the `Image Template` items on it and builds a list of those, with their cost.

Then it goes through all your current image templates, correlates the templates Storage_Repository, and child templates with what was on your last invoice, and does some very basic math to come up with a next month cost.

Be aware that the next month cost assumes the template has existed in the repository for the entire month. So the result this script returns may not match exactly with what is on your next bill. This script also is not able to estimate cost of images that have been delete in the current month.

```python
"""
Image template cost calculator.

SoftLayer stores image templates in a SoftLayer_Virtual_Storage_Repository, which has a collection of other templates.
You are billed per Storage_Repository, based on the images size on disk (not actual disk size).
An image template created mid-month will result in a smaller bill than calcualted. 
It is not possible for this script to pull usage data for images that have been deleted, so those are not included in these estimates.
Any entry in the CSV output that has a number for the first column means that Storage_Repo was delete since the last bill.
"""
 
import SoftLayer
from pprint import pprint as pp
import logging
import  click

 
class example():
 
    def __init__(self):
        """
       :param int start: epoch time to start at. Should align to 00:00 UTC
       :param int end: epoch time to end at. Should align to 00:00 UTC
       """
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger
 
        # logger = logging.getLogger()
        # logger.addHandler(logging.StreamHandler())
   
    def debug(self):
        """
        Useful for printing out the exact API calls that were used. If using the rest transport, will print cure-able commands.
        """
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))
 
    def main(self):
        """
        Goes through all image templates on your account and tries to figure out how much they will cost next month.
        These costs are ESTIMATES and assumes the image template exists on your account for the entire month.
        """

        storage_repos = self.lastInvoiceRepos()
        mask = """mask[children[blockDevicesDiskSpaceTotal,storageRepository[id,datacenter,name,metricTrackingObject,billingItem[item[activeUsagePrices]]]]]"""
        objects = self.client.call('Account', 'getPrivateBlockDeviceTemplateGroups', mask=mask, iter=True, limit=20)
        for _object in objects:

            for child in _object['children']:
                try:
                    repo_id = child['storageRepository']['id']
                    repo_name = child['storageRepository']['name']

                    metric_id = child['storageRepository']['metricTrackingObject']['id']
                    rate = float(child['storageRepository']['billingItem']['item']['activeUsagePrices'][0]['usageRate'])
                    size = self.convert(child['blockDevicesDiskSpaceTotal'])

                    if not storage_repos.get(repo_id):
                        storage_repos[repo_id] = {'images':[], 'name': repo_name}

                    storage_repos[repo_id]['name'] = "{} - {}".format(repo_id, repo_name)
                    storage_repos[repo_id]['images'].append({
                        'metricTrackingObject': metric_id,
                        'billingItemId': child['storageRepository']['billingItem']['id'],
                        'rate': rate, 
                        'size': size,
                        'name': child['name'],
                        'cost': round(size * rate, 2)
                    })
                except KeyError as e:
                    pass

        print("Valut, Last Cost, Next Cost, Size, Images")
        for repo in storage_repos:
            next_cost = []
            size = []
            images = []
            for image in storage_repos[repo]['images']:
                next_cost.append(image['cost'])
                size.append(image['size'])
                images.append(image['name'])

            print("{}, {}, {}, {}, {}".format(
                storage_repos[repo]['name'], storage_repos[repo]['recurringFee'],
                round(sum(next_cost),2), round(sum(size),2), ",".join(images)
            ))

    def lastInvoiceRepos(self):
        """Gets the last invoice and fines all the SoftLayer_Virtual_Storage_Repository items"""
        repos = {}
        invoice_mask = """mask[id]"""
        top_mask = """mask[category,billingItem,product]"""
        # Image Template Storage or Public Image Storage
        # Archive Storage Repository or Public Storage Repository
        _filter = {
            'invoiceTopLevelItems' : {
                'categoryCode': {
                    'operation': 'or',
                    'options': [{
                        'name': 'data',
                        'value': ['public_storage', 'guest_storage']
                    }]
                }
            }
        }

        invoice = self.client.call('SoftLayer_Account', 'getLatestRecurringInvoice', mask=invoice_mask)
        items = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTopLevelItems', mask=top_mask, 
                                 filter=_filter, iter=True, id=invoice['id'])
        for item in items:
            repos[item['resourceTableId']] = {
                'product': item['product']['description'],
                'recurringFee' :item['recurringFee'],
                'oneTimeFee': item['oneTimeFee'],
                'images': [],
                'name': item['resourceTableId']
            }

        return repos
 

    def convert(self, bytes):
        return  round(int(bytes) / (1024 **3 ),2)
 
@click.command()
def main():
    main = example()
    main.main()
    
    # Uncomment this to print out the API calls made.
    # main.debug()
 
if __name__ == "__main__":
    main()
```