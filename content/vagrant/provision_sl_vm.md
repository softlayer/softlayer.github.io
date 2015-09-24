---
title: "Provision a SoftLayer server from vagrant"
description: "Example of how to provision a SoftLayer server through Vagrant"
date: "2015-09-24"
tags:
  - "vagrant"
  - "provision"
---

#### Prerequisites

In addition to the prerequisites above, you will also require the *vagrant-softlayer* plugin.  Additionally, the following one-time setup steps must be performed:

+ Create a .softlayer file in the project root, containing your personal SoftLayer settings for:
    * api_key - your SoftLayer API key
    * user_name - Your SoftLayer user name
    * ssh_key - The identifying string of your SSH public key stored in SoftLayer (e.g., 'John Public Key'). Use the `slcli sshkey list` command to look at the keys loaded in the account.

    Note that the Vagrantfile currently assumes that the corresponding private key is stored in ~/.ssh/id_rsa, on the vagrant workstation

```json
{
  "api_key": "api-key",
  "username": "sl_user_name",
  "ssh_key": "stored_ssh_key_entry_name",
  "datacenter": "wdc01"
}
```

+ Create a metadata.json file with the following contents:
```json
{
    "provider": "softlayer"
}
```

+ Create the SoftLayer 'box' that includes the metadata file and install into Vagrant:
    tar cvzf softlayer.box metadata.json
    vagrant box add --name softlayer softlayer.box

+ Create a vagrant file with the softlayer provider settings included:
```ruby
sl_user_data_file = File.join(File.dirname(File.expand_path(__FILE__)), '.softlayer')
sl_user_data = JSON.parse(File.open(sl_user_data_file).read, :symbolize_names => true)

config.vm.provider :softlayer do |sl, config_override|
  config_override.vm.box = 'softlayer'
  config_override.ssh.username = 'root'
  config_override.ssh.private_key_path = [ File.expand_path("~/.ssh/id_rsa") ]

  sl.start_cpus = 2
  sl.max_memory = 4096
  sl.operating_system = 'UBUNTU_LATEST'

  sl_user_data.each do |k, v|
    sl.send("#{k}=", v)
  end
end
```

#### Deploy

Run the following:

`vagrant up --provider=softlayer`

This will spin up a new VM in SoftLayer.  You can `vagrant ssh`, `vagrant destroy`, etc. as normal.
