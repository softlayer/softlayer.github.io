---
title: "Get tickets using an objectFilter"
description: "Pulls down all the tickets created after a set date, and lasted update was by an employee of SoftLayer"
date: "2015-07-08"
classes: ["SoftLayer_Account"]
tags:
    - "tickets"
    - "objectFilter"
    - "objectMask"
    - "SOAP"
---

```php
<?php

require_once './SoftLayer/SoapClient.class.php';
$apiUser = '';
$key = '';

$startDate = new DateTime('2015-05-28T10:05:25-06:00');

$ticketClient = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $apiUser, $key);
$filter = new stdClass();
$filter->tickets = new stdClass();
$filter->tickets->updates = new stdClass();
$filter->tickets->updates->createDate = new stdClass();
$filter->tickets->updates->createDate->operation = 'greaterThanDate';
$filter->tickets->updates->createDate->options = array();
$filter->tickets->updates->createDate->options[0] = new stdClass();
$filter->tickets->updates->createDate->options[0]->name = 'date';
$filter->tickets->updates->createDate->options[0]->value = array($startDate->format('m/d/Y H:i:s'));
$filter->tickets->updates->editorType = new stdClass();
$filter->tickets->updates->editorType->operation = 'EMPLOYEE';

$mask = new SoftLayer_ObjectMask();
$mask->tickets->updates;

$ticketClient->setObjectMask($mask);
$ticketClient->setObjectFilter($filter);
$updates = $ticketClient->getTickets();

print_r($updates);

//prints out some SOAP debugging
print_r($ticketClient->__getLastRequest());
```