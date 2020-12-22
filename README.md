# softlayer.github.io - sldn.softlayer.com
This project is the HTML files for [SLDN](https://sldn.softlayer.com), the API documentation for IBM Classic Infrastructure service (aka SoftLayer).

The content here is broken down into the following sections.

#### [Articles](https://sldn.softlayer.com/article/)
Detailed explanations of core concepts of the API, with a few REST examples to illustrate how it all works.

#### [Automated Documentation](https://sldn.softlayer.com/reference/softlayerapi/)
Everything in here is automatically generated from the API source code, updated weekly with changes, usually reflected in the home page's [Change Log](https://sldn.softlayer.com/release_notes/)

A lot of this information is also available directly from the metadata of the SL API

```bash
 curl  -v -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/metadata/v3.1/'
```
For example:
```json
"SoftLayer_Account": {
    "name": "SoftLayer_Account",
    "base": "SoftLayer_Entity",
    "serviceDoc": "Every SoftLayer customer has an account which is defined in the SoftLayer_Account service. SoftLayer accounts have users, hardware, and services such as storage and domains associated with them. The SoftLayer_Account service is a convenient way to obtain general information about your SoftLayer account. Use the data returned by these methods with other API services to get more detailed information about your services and to make changes to your servers and services. \n\nSoftLayer customers are unable to change their company account information in the portal or the API. If you need to change this information please open a sales ticket in our customer portal and our account management staff will assist you. ",
    "methods": {
        "activatePartner": {
            "name": "activatePartner",
            "type": "SoftLayer_Account",
            "static": true,
            "maskable": true,
            "parameters": [
                {
                    "name": "accountId",
                    "type": "string",
                    "doc": "Specify the account ID that needs to be activated."
                },
                {
                    "name": "hashCode",
                    "type": "string",
                    "doc": "Specify the hashcode for the partner"
                }
            ]
        },
 ```
 
 #### Language Examples
 There are a few different language example sections, each containg a variety of usage examples on how to interact with the API through that language's SDK.
 
 
 
 ## Making Changes.
 This repo is generated from [githubio_source](https://github.com/softlayer/githubio_source), any changes need to be made there. 
 The only exception to this is the content in the "Documentation" section, which is generated elsewhere.
 
 ## Requesting Examples
 If you ever find yourself wishing there was an example of how to do something in the SoftLayer API, please make a github issue on the [githubio_source](https://github.com/softlayer/githubio_source/issues) repository.
 
 
 
