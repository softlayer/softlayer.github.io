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
```php
<?php

/* follow the installation instructions to get SoftLayer API PHP Client working: https://github.com/softlayer/softlayer-api-php-client#installation */
require_once __DIR__.'/vendor/autoload.php';

use SoftLayer\Common\ObjectMask;
use SoftLayer\SoapClient;

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = '';
$apiKey = '';
$packageId = 46;


$client = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', $packageId, $apiUsername, $apiKey);
try {
    $mask = new SoftLayer\Common\ObjectMask();
    $mask->configuration->itemCategory;
    $client->setObjectMask($mask);
    $configs = $client->getConfiguration();
    $requiredCategories = array();

    foreach ($configs as $config) {
        if ($config->isRequired == 1) {
            $requiredCategories[$config->itemCategory->id]['name'] = $config->itemCategory->name;
        }
    }
    $categories = array();
    $mask = new SoftLayer\Common\ObjectMask();
    $mask->itemPrices->categories;
    $client->setObjectMask($mask);
    $prices = $client->getItemPrices();

    foreach ($requiredCategories as $category => $categoryName) {
        $i = 0;
        foreach ($prices as $price) {
            foreach ($price->categories as $priceCategory) {
                if ($priceCategory->id == $category) {
                    $requiredCategories[$category]['itemPrices'][$i]['id'] = $price->id;
                    $requiredCategories[$category]['itemPrices'][$i]['description'] = $price->item->description;
                    asort($requiredCategories[$category]['itemPrices'][$i]);
                    asort($requiredCategories);
                    $i++;
                }
            }
        }
    }

    print_r($requiredCategories);
} catch ( Exception $e) {
    die( $e->getMessage());
}

?>
```
