---
title: "Order a vyatta server with placeOrder"
description: "Orders a vyatta server. The priceIds may be invalid now, please double check them before running."
date: "2015-07-08"
classes: ["SoftLayer_Product_Order"]
tags:
    - "ordering"
    - "vyatta"
    - "placeOrder"
---

```php
<?php

require_once './SoftLayer/SoapClient.class.php';
$apiUser = '';
$key = '';

$client = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $apiUser, $key);
$template = new stdClass();
$template_extra = new stdClass();
$template->packageId = 174;
$template->location  = 224092;
$template->quantity  = 1;
$template_extra->os = 21;  //vyatta
$template_extra->hostname = 'foo-vga-small';
$template_extra->domain = 'softlayer-singapore-test.com';

//These might be invalid now, please double check on ordering
$template_extra->price_id = array(13739, // Single Quad Xeon 1270 3.4G 8M
                                   21010, // 4G
                                   878, // Raid
                                   //31693, // Raid 1
                                   1267, // 500G
                                   274, // 1GbE
                                   342, // 20T
                                   // 21, // 1IP
                                   56, // Ping/TCP Mon
                                   57, // Notification 
                                   );

$my_template = new stdClass();

 for ($cnt = 0; $cnt < $template->quantity; $cnt++) {
    $domain = new stdClass();
    $domain->hostname = "$template_extra->hostname-$cnt";
    $domain->domain = $template_extra->domain;
    $template->hardware[] = $domain;
  }
if (empty($template->imageTemplateGlobalIdentifier))
{
    $template_extra->price_id[] = $template_extra->os;
}

foreach ($template_extra->price_id as $id) {
    $price = new stdClass();
    $price->id = $id;
    $template->prices[] = $price;
}
$my_template->orderContainers = array();
$my_template->orderContainers[0]->prices = $template->prices;
$my_template->orderContainers[0]->hardware = $template->hardware;
$my_template->orderContainers[0]->quantity = $template->quantity;
$my_template->orderContainers[0]->location = $template->location;
$my_template->orderContainers[0]->packageId = $template->packageId;

print_r($my_template);
$result = $client->verifyOrder($my_template);
print_r($result);
```