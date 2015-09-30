---
title: "Get primary ip address record"
description: "For a given virtual guest id, retrieve the information concerning its primary ip address"
date: "2015-01-03"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
    - "deprecated"
---
```php
<?php
require_once './SoftLayer/SoapClient.class.php';

$apiUsername = '';
$apiKey = '';
$virtualGuestId = 1111111
$client = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest',   $virtualGuestId, $apiUsername, $apiKey);


$objectMask = new SoftLayer_ObjectMask();
$objectMask->primaryNetworkComponent;
$objectMask->primaryNetworkComponent->primaryIpAddressRecord;

$client->setObjectMask($objectMask);
$guest = $client->getObject();
print_r($guest);



/*
=============== RESULT ===============
~/Code/softlayer-examples/testing/php  $ php getIpID.php
stdClass Object
(
    [accountId] => 307608
    [createDate] => 2015-06-12T15:37:58-06:00
    [dedicatedAccountHostOnlyFlag] =>
    [domain] => test.lablayer.info
    [fullyQualifiedDomainName] => salttest.test.lablayer.info
    [hostname] => salttest
    [id] => 10015277
    [lastPowerStateId] =>
    [lastVerifiedDate] =>
    [maxCpu] => 1
    [maxCpuUnits] => CORE
    [maxMemory] => 1024
    [metricPollDate] =>
    [modifyDate] => 2015-06-12T16:12:52-06:00
    [provisionDate] => 2015-06-12T15:42:03-06:00
    [startCpus] => 1
    [statusId] => 1001
    [uuid] => 7a9731a1-4c29-144b-8051-55507ff1f08b
    [globalIdentifier] => 8f5ed47b-9864-418b-8966-e9d4a70742f8
    [managedResourceFlag] =>
    [primaryBackendIpAddress] => 10.91.155.168
    [primaryIpAddress] => 198.23.82.198
    [primaryNetworkComponent] => stdClass Object
        (
            [createDate] => 2015-06-12T15:38:26-06:00
            [guestId] => 10015277
            [id] => 5277729
            [macAddress] => 06:51:99:7e:f9:ef
            [maxSpeed] => 10
            [modifyDate] => 2015-06-12T15:38:39-06:00
            [name] => eth
            [networkId] => 4043239
            [port] => 1
            [speed] => 10
            [status] => ACTIVE
            [uuid] => 61836774-e776-d480-75e5-bc45b74982c7
            [primaryIpAddress] => 198.23.82.198
            [primaryIpAddressRecord] => stdClass Object
                (
                    [id] => 13751854
                    [ipAddress] => 198.23.82.198
                    [isBroadcast] =>
                    [isGateway] =>
                    [isNetwork] =>
                    [isReserved] =>
                    [subnetId] => 469930
                    [guestNetworkComponentBinding] => stdClass Object
                        (
                            [ipAddressId] => 13751854
                            [port] =>
                            [type] => PRIMARY
                        )

                    [subnet] => stdClass Object
                        (
                            [broadcastAddress] => 198.23.82.199
                            [cidr] => 29
                            [gateway] => 198.23.82.193
                            [id] => 469930
                            [isCustomerOwned] =>
                            [isCustomerRoutable] =>
                            [modifyDate] => 2015-04-18T19:15:55-06:00
                            [netmask] => 255.255.255.248
                            [networkIdentifier] => 198.23.82.192
                            [networkVlanId] => 359732
                            [sortOrder] => 4
                            [subnetType] => PRIMARY
                            [totalIpAddresses] => 8
                            [usableIpAddressCount] => 5
                            [version] => 4
                        )

                )

        )

    [status] => stdClass Object
        (
            [keyName] => ACTIVE
            [name] => Active
        )

)
*/
```