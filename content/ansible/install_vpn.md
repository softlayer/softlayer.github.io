---
title: "Install the Array Networks VPN"
description: "Ansible playbook to install Array Networks command line VPN on Ubuntu. You can establish SSL VPN connections using the command sudo ./array_vpnc64 -hostname https://vpn.dal05.softlayer.com -username <sl_userid> -passwd <vpn_password>"
date: "2015-09-23"
tags:
  - "vpn"
  - "ubuntu"
---

```yaml
---
- hosts: all
  sudo: yes
  tasks:
    - name: Create directory for VPN client
      file:
        path: "~/vpn"
        state: directory

    - name: Get VPN binary file
      get_url:
        url: "http://speedtest.dal05.softlayer.com/array/ArrayNetworksL3VPN_LINUX.zip"
        dest: "~/vpn/ArrayNetworksL3VPN_LINUX.bin"
        sha256sum: "6300f97886bdabcd8e92d3327f2704b705dc0bd050b4fd9fb5dc8cb9ed6ceec2"

    - name: Add execute permissions on VPN client
      file:
        path: "~/vpn/ArrayNetworksL3VPN_LINUX.bin"
        mode: u=rwx

    - name: Extract VPN client files from binary
      command: "./ArrayNetworksL3VPN_LINUX.bin"
      args:
        chdir: "~/vpn"
        creates: "~/vpn/array_vpnc64"

    - name: Update permissions on the VPN client
      file:
        path: "~/vpn"
        mode: "u=rwX,g=rX,o=rX"
        recurse: yes
```
