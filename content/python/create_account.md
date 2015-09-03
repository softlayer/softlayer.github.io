---
title: "create child account!"
description: "lorem"
date: "2014-09-01"
categories:
  - "example"
  - "hello"
tags:
  - "example"
  - "hugo"
  - "blog"
---

```
# Create SoftLayer End-Customer Account on Brand Account
# Use at your own risk

import SoftLayer
from pprint import pprint as pp
import json
import SoftLayer.API

# DIST MASTER ACCOUNT API INFORMATION (NOT SUB-BRAND)
username = "CHANGE_ME" #change me
apiKey = "CHANGE_ME" #change me

# Brand ID of the Sub-brand to create the account under, NOT the top level distributor brand.
# Very important to set this correctly, as it determines the location of the account
# Will currently be a five digit number (the ID of of the parent brand, not the parent account)
brandId = 0 #change me

companyname = "" #change me
firstname = "" #change me
lastname = "" #change me
address = "" #change me
city = "" #change me
state = "" #change me
country = "" #change me -- two letter ISO code
zipcode = "" #change me
phone = "" #change me
email = "" #change me

cust_account = {
 "brandId": brandId,
 "companyName": companyname,
 "firstName": firstname,
 "lastName": lastname,
 "address1": address,
 "postalCode": zipcode,
 "city": city,
 "state": state,
 "country": country,
 "officePhone": phone,
 "email": email,
 "lateFeeProtectionFlag": True,
 "claimedTaxExemptTxFlag": False,
 "allowedPptpVpnQuantity": 1,
 "isReseller": 0,
 "accountStatusId": 1001 # 1001 = Active Account
}

print("\n")
pp(cust_account)
print("\n")
null = raw_input("Press Enter to create this brand in production... This cannot be undone.")
print("\n")

client = SoftLayer.Client(
   username= username,
   api_key = apiKey,
   )

try:
   result = client['Brand'].createCustomerAccount(cust_account)
   print ()
   print ("Result = ", json.dumps(result, indent=2))
except SoftLayer.SoftLayerAPIError as e:
   print("Error: %s, %s" % (e.faultCode, e.faultString))
   exit()
```

