---
title: "Create an A record method 2"
description: "Adds an A record to a DNS zone using url parameters"
date: "2015-05-30"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---

To start off, get the id of the domain you want to add the record to.

Operation: `GET`

Method: [`SoftLayer_Dns_Domain::getByDomainName()`](http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getByDomainName)

URL: `SoftLayer_Dns_Domain/getByDomainName/domain.com`

Example CURL: `curl -u username:api_key "https://api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/getByDomainName/domain.com"`

Example Response:
```json
[{"id":123456789,"name":"domain.com","serial":2015092400,"updateDate":"2015-09-24T13:46:20-06:00"},{"id":1795354,"name":"global.domain.com","serial":2015050613,"updateDate":"2015-05-06T14:47:45-06:00"}]
```


------
Now we just need to create the record

Operation: `POST`

Method: [`SoftLayer_Dns_Domain_ResourceRecord::createObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject)

URL: `SoftLayer_Dns_Domain_ResourceRecord`

Example CURL: `curl -u username:api_key "https://api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/123456789/createARecord/testing/184.172.7.100/500"`

Example Response:
```json
{"data":"184.172.7.100","domainId":123456789,"expire":null,"host":"testing","id":58406111,"minimum":null,"mxPriority":null,"refresh":null,"retry":null,"ttl":86400,"type":"A","domain":{"id":123456789,"name":"domain.com","serial":2015092401,"updateDate":"2015-09-24T15:51:41-06:00"}}
```

