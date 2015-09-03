---
title: "Cancel software licenses by IP"
description: "Cancel all software licenses associated with a specific IPv4 address"
date: "20-3-09-01"
classes: ["SoftLayer_Account", "SoftLayer_Billing_Item_Cancellation_Request"]
tags:
  - "license"
  - "cancel"
  - "billing"
  - "deprecated"
---

```
#!/usr/bin perl
use warnings;
use strict;
use Data::Dumper;
use SoftLayer::API::SOAP;

my $api_username = '';
my $api_key = '';

my $cPanelIp = '127.0.0.1';
my $billingItemId;
my $accountId;

my $accountClient = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);
my $billingClient = SoftLayer::API::SOAP->new('SoftLayer_Billing_Item_Cancellation_Request', undef, $api_username, $api_key);

my $objectMask = "mask.billingItem.id";
$accountClient->setObjectMask($objectMask);

my $licenses = $accountClient->getActiveVirtualLicenses()->result;

for my $i (0 .. $#{$licenses}) {
    my $license = $licenses->[$i];
    if ($cPanelIp eq $license->{'ipAddress'}) {
        $billingItemId = $license->{'billingItem'}->{'id'};
        $accountId = $license->{'accountId'};
    }
}

my $cancellationRequestTemplateObject = {
    'items' => [
            {
                'billingItemId' => $billingItemId,
            }
    ],
    'accountId' => $accountId
};

my $result = $billingClient->createObject($cancellationRequestTemplateObject);
print Dumper($result);
```
