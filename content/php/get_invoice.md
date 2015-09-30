---
title: "Get Invoices"
description: "Get all invoices for a given date range"
date: "2015-02-22"
classes: ["SoftLayer_Account"]
tags:
    - "billing"
    - "invoice"
    - "objectMask"
    - "objectFilter"
    - "deprecated"
---


```php
<?php
require_once './SoftLayer/SoapClient.class.php';
 
$apiUser = '';
$key = '';

//The date does need to be in this specific format
$startDate = new DateTime('2014-11-01T13:05:25-06:00');
$endDate = new DateTime('2014-12-01T09:53:51-06:00');
 
$accountClient = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $apiUser, $key);

$filter = new stdClass();
$filter->invoices = new stdClass();
// $filter->invoices->accountId = new stdClass();
// $filter->invoices->accountId->operation = '= 391780';
$filter->invoices->createDate = new stdClass();
$filter->invoices->createDate->operation = 'betweenDate';
$filter->invoices->createDate->options = array();
$filter->invoices->createDate->options[0] = new stdClass();
$filter->invoices->createDate->options[0]->name = 'startDate';
$filter->invoices->createDate->options[0]->value = array($startDate->format('m/d/Y H:i:s'));
$filter->invoices->createDate->options[1] = new stdClass();
$filter->invoices->createDate->options[1]->name = 'endDate';
$filter->invoices->createDate->options[1]->value = array($endDate->format('m/d/Y H:i:s'));

$objectMask = new SoftLayer_ObjectMask();
$objectMask->invoices; 
 
$accountClient->setObjectFilter($filter);
$accountClient->setObjectMask($objectMask);

$invoices = $accountClient->getObject();

print_r($invoices);

```