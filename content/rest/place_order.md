---
title: "Ordering with placeOrder"
description: "Example on how to call verifyOrder / placeOrder via REST. Replace the veryifyOrder call with placeOrder when you are actually ready to order the server"
date: "2015-09-30"
classes: ["SoftLayer_Product_Order"]
tags:
  - "ordering"
  - "placeOrder"
  - "objectMask"
---

Operation: `POST`

Method: [`SoftLayer_Product_Order::placeOrder()`](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/)

URL: SoftLayer_Product_Order/verifyOrder`

Example CURL: 
```
curl -u userid:api_key -X POST --data @create.json 
https://api.softlayer.com/rest/v3/SoftLayer_Product_Order/verifyOrder
```


Input JSON:
```json
{
    "parameters" : [
        {
            "packageId" : 126,
            "location" :449494,
            "quantity" : 1,
            "hardware": [{
                "hostname": "TEST",
                "domain": "test1"
            }],
            "prices": [
                {"id": 13739},
                {"id": 13748},
                {"id": 1267},
                {"id": 342},
                {"id": 21141},
                {"id": 58},
                {"id": 876},
                {"id": 57},
                {"id": 55},
                {"id": 21},
                {"id": 906},
                {"id": 420},
                {"id": 418},
                {"id": 37620}
            ]
        }
    ]
}
```

The price ids explained.
```json
    #Single Processor Quad Core Xeon 1270 - 3.40GHz (Sandy Bridge) - 1 x 8MB cache w/HT
    {'id': 13739},
    #32 GB DDR3 1333
    {'id': 13748},
    #1TB sataII
    {'id': 1267},
    #2000 GB Bandwidth
    {'id': 342},
    #1 Gbps Dual public uplink
    {'id': 21141},
    #automated notification response
    {'id': 58},
    #Non-Raid Disk Controller
    {'id': 876},
    #email and ticket notification
    {'id': 57},
    #host ping monitoring
    {'id': 55},
    #single primary ip
    {'id': 21},
    #remote managements
    {'id': 906},
    #vpn management
    {'id': 420},
    #vulnerability 
    {'id': 418},
    #Ubuntu 14.04 64bit
    {'id': 37620}
```

Example Response:
```json
{
    "bigDataOrderFlag": false,
    "billingOrderItemId": null,
    "containerSplHash": "000000004f26de1000007f7b4154b39b",
    "currencyShortName": "USD",
    "extendedHardwareTesting": null,
    "hardware": [
        {
            "accountId": null,
            "bareMetalInstanceFlag": null,
            "domain": "test1",
            "hardwareStatusId": null,
            "hostname": "TEST",
            "primaryBackendNetworkComponent": {
                "networkVlanId": null
            },
            "primaryNetworkComponent": {
                "networkVlanId": null
            }
        }
    ],
    "imageTemplateId": null,
    "isManagedOrder": 0,
    "location": "449494",
    "locationObject": {
        "id": 449494,
        "longName": "Dallas 9",
        "name": "dal09"
    },
    "message": "",
    "monitoringAgentConfigurationTemplateGroupId": null,
    "packageId": 126,
    "paymentType": "",
    "postTaxRecurring": "0",
    "postTaxRecurringHourly": "0",
    "postTaxRecurringMonthly": "0",
    "postTaxSetup": "0",
    "preTaxRecurring": "0",
    "preTaxRecurringHourly": "0",
    "preTaxRecurringMonthly": "0",
    "preTaxSetup": "0",
    "presetId": null,
    "prices": [
        {
            "categories": [
                {
                    "categoryCode": "server",
                    "id": 1,
                    "name": "Server"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 13739,
            "item": {
                "bundle": [],
                "capacity": "3.4",
                "description": "Single Intel Xeon E3-1270 (4 Cores, 3.40 GHz)",
                "id": 3796,
                "keyName": "INTEL_SINGLE_XEON_1270_3_40_2",
                "units": "GHz"
            },
            "itemId": 3796,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "ram",
                    "id": 3,
                    "name": "RAM"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 13748,
            "item": {
                "bundle": [],
                "capacity": "32",
                "description": "32 GB DDR3 1333",
                "id": 3805,
                "keyName": "RAM_32_GB_DDR3_1333_NON_REG",
                "units": "GB"
            },
            "itemId": 3805,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "disk0",
                    "id": 4,
                    "name": "First Hard Drive"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 1267,
            "item": {
                "bundle": [],
                "capacity": "500",
                "description": "500 GB SATA ",
                "id": 14,
                "keyName": "HARD_DRIVE_500GB_SATA_II",
                "units": "GB"
            },
            "itemId": 14,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "bandwidth",
                    "id": 10,
                    "name": "Public Bandwidth"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 342,
            "item": {
                "bundle": [],
                "capacity": "20000",
                "description": "20000 GB Bandwidth",
                "id": 249,
                "keyName": "BANDWIDTH_20000_GB",
                "units": "GB"
            },
            "itemId": 249,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "port_speed",
                    "id": 26,
                    "name": "Uplink Port Speeds"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 21141,
            "item": {
                "bundle": [
                    {
                        "bundleItem": {
                            "capacity": "1000",
                            "description": "1 Gbps Dual Public & Private Network Uplinks (Unbonded)",
                            "id": 4263,
                            "keyName": "1_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED",
                            "units": "Mbps"
                        },
                        "bundleItemId": 4263,
                        "category": {
                            "categoryCode": "service_port",
                            "id": 9,
                            "name": "Private Network Port"
                        },
                        "id": 5544,
                        "itemPrice": {
                            "id": 22235,
                            "itemId": 4399,
                            "laborFee": "0",
                            "oneTimeFee": "0",
                            "recurringFee": "0",
                            "setupFee": "0"
                        },
                        "itemPriceId": 22235
                    },
                    {
                        "bundleItem": {
                            "capacity": "1000",
                            "description": "1 Gbps Dual Public & Private Network Uplinks (Unbonded)",
                            "id": 4263,
                            "keyName": "1_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED",
                            "units": "Mbps"
                        },
                        "bundleItemId": 4263,
                        "category": {
                            "categoryCode": "public_port",
                            "id": 8,
                            "name": "Public Network Port"
                        },
                        "id": 6400,
                        "itemPrice": {
                            "hourlyRecurringFee": "0",
                            "id": 22233,
                            "itemId": 4400,
                            "laborFee": "0",
                            "oneTimeFee": "0",
                            "recurringFee": "0",
                            "setupFee": "0"
                        },
                        "itemPriceId": 22233
                    }
                ],
                "capacity": "1000",
                "description": "1 Gbps Dual Public & Private Network Uplinks (Unbonded)",
                "id": 4263,
                "keyName": "1_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED",
                "units": "Mbps"
            },
            "itemId": 4263,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "response",
                    "id": 22,
                    "name": "Response"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 58,
            "item": {
                "bundle": [],
                "description": "Automated Notification",
                "id": 52,
                "keyName": "AUTOMATED_NOTIFICATION"
            },
            "itemId": 52,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "disk_controller",
                    "id": 11,
                    "name": "Disk Controller"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 876,
            "item": {
                "bundle": [],
                "description": "Non-RAID",
                "id": 487,
                "keyName": "DISK_CONTROLLER_NONRAID"
            },
            "itemId": 487,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "notification",
                    "id": 21,
                    "name": "Notification"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 57,
            "item": {
                "bundle": [],
                "description": "Email and Ticket",
                "id": 51,
                "keyName": "NOTIFICATION_EMAIL_AND_TICKET"
            },
            "itemId": 51,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "monitoring",
                    "id": 20,
                    "name": "Monitoring"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 55,
            "item": {
                "bundle": [],
                "description": "Host Ping",
                "id": 49,
                "keyName": "MONITORING_HOST_PING"
            },
            "itemId": 49,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "pri_ip_addresses",
                    "id": 13,
                    "name": "Primary IP Addresses"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 21,
            "item": {
                "bundle": [],
                "capacity": "1",
                "description": "1 IP Address",
                "id": 15,
                "keyName": "1_IP_ADDRESS"
            },
            "itemId": 15,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "remote_management",
                    "id": 46,
                    "name": "Remote Management"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 906,
            "item": {
                "bundle": [],
                "description": "Reboot / KVM over IP",
                "id": 504,
                "keyName": "REBOOT_KVM_OVER_IP"
            },
            "itemId": 504,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "vpn_management",
                    "id": 31,
                    "name": "VPN Management - Private Network"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 420,
            "item": {
                "bundle": [],
                "description": "Unlimited SSL VPN Users & 1 PPTP VPN User per account",
                "id": 309,
                "keyName": "UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT"
            },
            "itemId": 309,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "vulnerability_scanner",
                    "id": 32,
                    "name": "Vulnerability Assessments & Management"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 418,
            "item": {
                "bundle": [],
                "description": "Nessus Vulnerability Assessment & Reporting",
                "id": 307,
                "keyName": "NESSUS_VULNERABILITY_ASSESSMENT_REPORTING"
            },
            "itemId": 307,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        },
        {
            "categories": [
                {
                    "categoryCode": "os",
                    "id": 12,
                    "name": "Operating System"
                }
            ],
            "hourlyRecurringFee": "0",
            "id": 37620,
            "item": {
                "bundle": [],
                "capacity": "0",
                "description": "Ubuntu Linux 14.04 LTS Trusty Tahr - Minimal Install (64 bit)",
                "id": 4710,
                "keyName": "OS_UBUNTU_14_04_LTS_TRUSTY_TAHR_MINIMAL_64_BIT_2",
                "units": "N/A"
            },
            "itemId": 4710,
            "laborFee": "0",
            "oneTimeFee": "0",
            "recurringFee": "0",
            "setupFee": "0"
        }
    ],
    "primaryDiskPartitionId": 1,
    "privateCloudOrderFlag": false,
    "proratedInitialCharge": "0",
    "proratedOrderTotal": "0",
    "quantity": 1,
    "resourceGroupId": null,
    "resourceGroupTemplateId": null,
    "sendQuoteEmailFlag": null,
    "serverCoreCount": 4,
    "sourceVirtualGuestId": null,
    "stepId": null,
    "taxCacheHash": "fa1c610dbd007f2b0fda6c417252d748bc093080",
    "taxCompletedFlag": true,
    "totalRecurringTax": "0",
    "totalSetupTax": "0",
    "useHourlyPricing": false
}
```

