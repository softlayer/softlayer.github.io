---
title: "Basic Rest Examples 2"
description: "A collection of some of the ways to interact with the REST service"
date: "2015-09-30"
classes: 
    - "SoftLayer_Account"
tags:
    - "objectMask"
---

Operation: `GET`

Method: [`SoftLayer_Account::getHardware()`](http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)

URL: `SoftLayer_Account/getHardware`

Parameters `objectMask=mask[id,fullyQualifiedDomainName,networkComponents[name,networkHardware[hostname],uplinkComponent[name,status]]]`

Example CURL: `curl -u username:api_key -G --data "objectMask=mask[id,fullyQualifiedDomainName,networkComponents[name,networkHardware[hostname],uplinkComponent[name,status]]]"  "https://api.softlayer.com/rest/v3/SoftLayer_Account/getHardware"`

Example Response:
```json
[
    {
        "fullyQualifiedDomainName": "bsdal5167180245106688.bsd.citrix.dc",
        "id": 115628,
        "networkComponents": [
            {
                "name": "mgmt",
                "networkHardware": [
                    {
                        "hostname": "bms173.sr03.dal05"
                    },
                    {
                        "hostname": "bcs173b.sr03.dal05"
                    },
                    {
                        "hostname": "bas08b.sr03.dal05"
                    },
                    {
                        "hostname": "bcr03b.dal05"
                    },
                    {
                        "hostname": "bcr03a.dal05"
                    },
                    {
                        "hostname": "bcs173a.sr03.dal05"
                    },
                    {
                        "hostname": "bas08a.sr03.dal05"
                    }
                ],
                "uplinkComponent": {
                    "name": "Ethernet1",
                    "status": "ACTIVE"
                }
            },
            {
                "name": "eth",
                "networkHardware": [
                    {
                        "hostname": "bcs173a.sr03.dal05"
                    },
                    {
                        "hostname": "bas08a.sr03.dal05"
                    },
                    {
                        "hostname": "bcr03b.dal05"
                    },
                    {
                        "hostname": "bcr03a.dal05"
                    }
                ],
                "uplinkComponent": {
                    "name": "GigabitEthernet1/0",
                    "status": "ACTIVE"
                }
            },
            {
                "name": "eth",
                "networkHardware": [
                    {
                        "hostname": "fcs173a.sr03.dal05"
                    },
                    {
                        "hostname": "fas08a.sr03.dal05"
                    },
                    {
                        "hostname": "fcr03a.dal05"
                    },
                    {
                        "hostname": "fcr03b.dal05"
                    }
                ],
                "uplinkComponent": {
                    "name": "GigabitEthernet1/0",
                    "status": "ACTIVE"
                }
            },
            {
                "name": "eth",
                "networkHardware": [
                    {
                        "hostname": "bcs173b.sr03.dal05"
                    },
                    {
                        "hostname": "bas08b.sr03.dal05"
                    },
                    {
                        "hostname": "bcr03b.dal05"
                    },
                    {
                        "hostname": "bcr03a.dal05"
                    }
                ],
                "uplinkComponent": {
                    "name": "GigabitEthernet2/0",
                    "status": "DISABLED"
                }
            },
            {
                "name": "eth",
                "networkHardware": [
                    {
                        "hostname": "fcs173b.sr03.dal05"
                    },
                    {
                        "hostname": "fas08b.sr03.dal05"
                    },
                    {
                        "hostname": "fcr03a.dal05"
                    },
                    {
                        "hostname": "fcr03b.dal05"
                    }
                ],
                "uplinkComponent": {
                    "name": "GigabitEthernet2/0",
                    "status": "DISABLED"
                }
            }
        ]
    }
]
```

