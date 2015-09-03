---
title: "Retrieve metric data for a single server."
description: "
 This example shows how to use the SoftLayer API to retrieve metric data for
 Advanced Monitoring on a single hardware or virtual guest server instance."
date: "2014-09-01"
classes: ["SoftLayer_Monitoring_Agent", "SoftLayer_Hardware_Server"]
tags:
  - "monitoring"
  - "metrics"
---
We will call the SoftLayer API to retrieve the monitoring agents,
 configuration template, and configuration values for a server instance.
 Then we will demonstrate how to find definitions that you have enabled for
 metric tracking, how to check that they are enabled, and how to then use them
 to get metrics for arbitrary dates.

 Note that the agent, section, sub-section, and definition names have already been
 pre-selected and in order for this example to work your server must have these
 configuration options enabled and be able to retrieve metrics for them through
the portal. If you wish to use additional or substitute names for any of those
shown below you can do so by looking at the current options available in the
 SoftLayer portal or by further debugging the output of this script.
```
<?php
 
// Include XmlrpcClient.class.php if you'd like to use our XML-RPC client
// instead.
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Your SoftLayer API username.
 *
 * @var string
 */
$apiUsername = 'set me!';

/**
 * Your SoftLayer API key. Generate and API key at the SoftLayer customer
 * portal:
 * https://manage.softlayer.com/Administrative/apiKeychain
 *
 * @var string
 */
$apiKey = 'set me too!';

/**
 * The id number of the server whose metrics you wish to retrieve. Call the
 * getVirtualGuests() method in the SoftLayer_Account API service to retrieve a list
 * of the servers on your account.
 *
 * @var int
 */
$serverId = 1234;

/**
 * The date at which you wish to start the metric sample. Pass any string that
 * is compatible with the PHP strtotime() function.
 *
 * @var string
 */
$startDate = '03/01/2014';

/**
 * The date at which you wish to end the metric sample.
 *
 * @var string
 */
$endDate = '03/02/2014';

/**
 * For this example we'll be working with SoftLayer_Virtual_Guest, you can also work
 * with SoftLayer_Hardware_Server depending on the type of server you're interacting with.
 *
 * Create a connection to the SoftLayer_Virtual_Guest API service and call the
 * getMonitoringAgents() method to get the server's associated tracking object record.
 */
$client = Softlayer_SoapClient::getClient('SoftLayer_Virtual_Guest', $serverId, $apiUsername, $apiKey);

try {
    // getMonitoringAgents() returns an array of SoftLayer_Monitoring_Agent objects.
    // From here you can loop through these agents to perform different functions such as get graphs,
    // activate, deactivate, or run other functions on it.
    $monitoringAgents = $client->getMonitoringAgents();
} catch (Exception $e) {
    die('Unable to retrieve server record: ' . $e->getMessage());
}

/**
 * Find the id of the specific agent we are wanting, in this example the "Cpu, Disk, and Memory" monitoring agent.
 */
$cdmAgent = null;
foreach ($monitoringAgents as $agent) {
    if ($agent->name == 'Cpu, Disk, and Memory Monitoring Agent') {
        $cdmAgent = $agent;
        break;
    }
}

/**
 * Next we can create an array of all configuration variables that we are able to track.
 * Re-declare our client variable to talk to the
 * SoftLayer_Monitoring_Agent API service.
 */
$client = SoftLayer_SoapClient::getClient('SoftLayer_Monitoring_Agent', $cdmAgent->id, $apiUsername, $apiKey);

// Object mask to get all definitions that we need.
$objectMask = 'mask.definition.monitoringDataFlag';
$client->setObjectMask($objectMask);

try {
    // getConfigurationValues() returns an array of
    // SoftLayer_Monitoring_Agent_Configuration_Value objects.
    $cdmConfigurationValues = $client->getConfigurationValues();
} catch (Exception $e) {
    die('Unable to retrieve monitoring agent configuration template: ' . $e->getMessage());
}

/**
 * SoftLayer_Monitoring_Agent_Configuration_Value is used to retrieve metric data types.
 * Check if the agent configuration value for each definition
 * has been enabled. Otherwise, we will not have any metric data.
 */
// Define the containers to hold the metric data types we will retrieve
$metricDataTypes = array();

foreach ($cdmConfigurationValues as $configurationValue) {

    // Ensure that this value is set to true
    if ((bool) $configurationValue->value == false) {
        continue;
    }

    // Ensure that the monitoring data flag is true
    if ($configurationValue->definition->monitoringDataFlag !== true) {
        continue;
    }

    // Get the metricDataType for this configuration value
    $client = SoftLayer_SoapClient::getClient('SoftLayer_Monitoring_Agent_Configuration_Value', $configurationValue->id, $apiUsername, $apiKey);
    try {
        $metricDataTypes[] = $client->getMetricDataType();
    } catch (Exception $e) {
        die('Unable to retrieve metric data type: ' . $e->getMessage());
    }
}

/**
 * Retrieving data for an individual metric.
 *
 * Re-declare our client variable to talk to the
 * SoftLayer_Monitoring_Agent API service.
 *
 * We will be retrieving the "Graph Total CPU Usage" metric data.
 */
$client = SoftLayer_SoapClient::getClient('SoftLayer_Monitoring_Agent', $cdmAgent->id, $apiUsername, $apiKey);

try {
    // getGraphData() returns a SoftLayer_Metric_Tracking_Object_Data object.
    $data = $client->getGraphData($metricDataTypes, $startDate, $endDate);
    echo "Data retrieved! " . count($data) . " data points\n\r";
} catch (Exception $e) {
    die('Unable to retrieve metric data: ' . $e->getMessage());
}
```
