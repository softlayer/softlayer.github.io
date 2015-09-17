---
title: "List Instances"
description: "Shows how to use one of the python client's managers, VSManager.list_instances() specifically"
date: "2015-01-01"
tags:
    - "manager"
---

```python
import SoftLayer
import pprint

class example():

    def __init__(self):

        self.client = SoftLayer.Client()
        self.mgr = SoftLayer.VSManager(self.client)

    def main(self):
        """

        """
        pp = pprint.PrettyPrinter(indent=4)
        result =  self.mgr.list_instances()
        pp.pprint(result)

if __name__ == "__main__":
    main = example()
    main.main()
```