---
title: "Get hostnames"
description: "Calls SoftLayer_Account::getObject with an objectMask to pull in all the hostnames for both hardware and virtual servers. Uses the . and ; format for object Masks."
date: "2015-09-30"
classes: 
    - "SoftLayer_Account"
tags:
    - "objectMask"
---
Operation: `GET`

Method: [`SoftLayer_Account::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Account/getObject)

URL: `SoftLayer_Account/getObject?objectMask=hardware.hostname;hourlyVirtualGuests.hostname;hourlyVirtualGuests.domain"`

Example CURL: ` curl -u username:api_key "https://api.softlayer.com/rest/v3/SoftLayer_Account/getObject?objectMask=hardware.hostname;hourlyVirtualGuests.hostname;hourlyVirtualGuests.domain"`

Example Response:
```json
{
    "accountManagedResourcesFlag": false,
    "accountStatusId": 1001,
    "address1": "4849 Alpha Rd",
    "allowedPptpVpnQuantity": 1,
    "brandId": 2,
    "city": "Dallas",
    "claimedTaxExemptTxFlag": false,
    "companyName": "SoftLayer Internal - Development Community",
    "country": "US",
    "createDate": "2014-02-04T10:33:56-06:00",
    "email": "asd@softlayer.com",
    "firstName": "Phil",
    "hardware": [
        {
            "hostname": "bsdal5167180245106688"
        },
        {
            "hostname": "db-server"
        },
        {
            "hostname": "db-server"
        },
        {
            "hostname": "deleteme"
        },
        {
            "hostname": "pjacksontestorder"
        }
    ],
    "hourlyVirtualGuests": [
        {
            "domain": "lablayer.info",
            "hostname": "api-lab"
        },
        {
            "domain": "sec.ibm.com",
            "hostname": "dal09-tst-eos-01a"
        },
        {
            "domain": "example.com",
            "hostname": "host1"
        },
        {
            "domain": "test.com",
            "hostname": "hostnametest-44ea"
        },
        {
            "domain": "test.com",
            "hostname": "hostnametest-6f6a"
        },
        {
            "domain": "test.com",
            "hostname": "hostnametest-709f"
        },
        {
            "domain": "test.com",
            "hostname": "hostnametest-7c92"
        },
        {
            "domain": "oeg.dal.slcommunity.org",
            "hostname": "oeg-es1"
        },
        {
            "domain": "oeg.dal.slcommunity.org",
            "hostname": "oeg-es2"
        }
    ],
    "id": 307608,
    "isReseller": 0,
    "lastName": "Asd",
    "lateFeeProtectionFlag": true,
    "modifyDate": "2014-02-04T10:34:18-06:00",
    "officePhone": "281.714.1234",
    "postalCode": "75244-4608",
    "state": "TX",
    "statusDate": null
}
```


