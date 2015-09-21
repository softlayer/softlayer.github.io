---
title: "Get top level billing items for all owned accounts"
description: "With a given date range, get all the invoice details for all of the owned brands, and all of their owned accounts. The $filter can be used to get just a single accounts invoices, just take off the ->allOwnedAccounts bits"
date: "2015-05-24"
classes: ["SoftLayer_Brand", "SoftLayer_Account", "SoftLayer_Billing_Invoice"]
tags:
    - "billing"
    - "objectFilter"
    - "objectMask"
    - "invoice"
    - "brand"
---


```php
<?php
require_once './SoftLayer/SoapClient.class.php';


/**
* This class structure is mostly used so this can be run as a script.
* Most of the print statements use fancy bash color codes to make things pretty
*/
class topBillingItems
{

    function __construct() {
        $this->apiUsername = '';
        $this->apiKey = '';
        $this->startDate = new DateTime('2015-02-12T00:00:00-06:00');
        $this->endDate = new DateTime('2015-03-12T00:00:00-06:00');
    }

    /*!
    * Will get all the brands on an account, THEN all of those brand's accounts,
    * Then all of THEIR brands, then all of THEIR accounts. Then, go through each
    * of the final tier accounts, and get all the invoices, then all the billing items.
    *
    */
    function main() {

        //The First Object Mask. Used to get all the front line brands, which will have the
        //accounts that are actually buying things
        $objectMask = new SoftLayer_ObjectMask();
        $objectMask->ownedBrands->allOwnedAccounts->ownedBrands;

        $client = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $this->apiUsername, $this->apiKey);
        $client->setObjectMask($objectMask);

        $response = $client->getObject();

        //Start off with the main brand
        foreach ($response->ownedBrands as $brand) {
            print "BRAND=\e[31m" . $brand->keyName .  " ::" . $brand->id . "\e[0m=\n";

            //Go into each of the top brands accounts
            foreach ($brand->allOwnedAccounts as $account) {
                print "==\e[32m" . $account->companyName ."\e[0m\n";

                //Go into each of those accounts brands...
                foreach ($account->ownedBrands as $brand1) {
                    print "====\e[33m" . $brand1->name ." ::" . $brand1->id . "\e[0m\n";
                    $brandInvoice = $this->getAllBrandAccounts($brand1->id);

                    //Go through each of the accounts on the brand
                    foreach ($brandInvoice as $brandAccount) {

                        //This is recursive and a very large data structure.
                        //we unset it here so it doesn't get in the way later
                        unset($brandAccount->brand);
                        $this->workAccount($brandAccount);

                    } //END foreach $brandInvoice
                } //END foreach $account->ownedBrands
            } //END foreach $brand->allOwnedAccounts
        } //END foreach $response->ownedBrands
    }//END MAIN

    function getAllBrandAccounts($brandId) {

        //This filters out all invoices that are not in our date range.
        //all based on the invoices createDate
        $filter = new stdClass();
        $filter->allOwnedAccounts = new stdClass();
        $filter->allOwnedAccounts->invoices = new stdClass();
        $filter->allOwnedAccounts->invoices->createDate = new stdClass();
        $filter->allOwnedAccounts->invoices->createDate->operation = 'betweenDate';
        $filter->allOwnedAccounts->invoices->createDate->options = array();
        $filter->allOwnedAccounts->invoices->createDate->options[0] = new stdClass();
        $filter->allOwnedAccounts->invoices->createDate->options[0]->name = 'startDate';
        $filter->allOwnedAccounts->invoices->createDate->options[0]->value = array($this->startDate->format('m/d/Y H:i:s'));
        $filter->allOwnedAccounts->invoices->createDate->options[1] = new stdClass();
        $filter->allOwnedAccounts->invoices->createDate->options[1]->name = 'endDate';
        $filter->allOwnedAccounts->invoices->createDate->options[1]->value = array($this->endDate->format('m/d/Y H:i:s'));

        //Mask for the front line brands, used to get all their accounts, and their invoices
        $brandMask = new SoftLayer_ObjectMask();
        $brandMask->allOwnedAccounts->invoices;

        //From that brand, get all the brand's owned accounts, with their invoices from the current month
        $brandClient = SoftLayer_SoapClient::getClient('SoftLayer_Brand', $brandId, $this->apiUsername, $this->apiKey);
        $brandClient->setObjectMask($brandMask);
        $brandClient->setObjectFilter($filter);
        return $brandClient->getAllOwnedAccounts();

    }

    function workAccount($account) {

        print "=====\e[94m" . $account->companyName ." ::" . $account->id . "\e[0m\n";
        //Used to get all the actual line items from an invoice
        $invoiceMask = new SoftLayer_ObjectMask();
        $invoiceMask->items;
        $invoiceMask->invoiceTotalAmount;
        //Go through each of the accounts monthly invoices
        foreach ($account->invoices as $invoice) {
            print "Created: " . $invoice->createDate . " TYPE: " . $invoice->typeCode ."\n";

            //Here we get the actual invoice and all the billing items inside of it
            $bClient = SoftLayer_SoapClient::getClient('SoftLayer_Billing_Invoice', $invoice->id , $this->apiUsername, $this->apiKey);
            $bClient->setObjectMask($invoiceMask);
            $bt = $bClient->getObject();
            print "====\e[42;90m" . $bt->invoiceTotalAmount ."\e[0m\n";

            //Go through each item on the invoice and print out its decription + fee.
            //There are a few other fields that could be billable, but these are the main ones.
            foreach ($bt->items as $lineItem) {
                unset($lineItem->invoice);
                $fee = $lineItem->recurringAfterTaxAmount + $lineItem->oneTimeAfterTaxAmount;
                print "====\e[35m" . $lineItem->description . " => " . $fee . "$ \e[0m\n";
            }

        }//end invoice
    }
}

$main = new Example();
$main->main();
```