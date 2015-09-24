---
title: "Install the SoftLayer CLI"
description: "Ansible playbook to install the SoftLayer CLI using pip on Ubuntu"
date: "2015-09-23"
tags:
  - "cli"
  - "ubuntu"
---

```yaml
- hosts: all
  sudo: yes
  tasks:
    - name: Update apt cache
      apt: update_cache=yes

    - name: Install pip for the install of the CLI
      apt:
        pkg: "{{ item }}"
        state: present
      when: ansible_os_family == 'Debian'
      with_items:
        - python-virtualenv
        - python-setuptools
        - python-pip

    - name: Install the SoftLayer CLI
      pip:
        name: softlayer
```
