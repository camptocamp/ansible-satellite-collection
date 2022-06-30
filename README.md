# Ansible Collection - camptocamp.satellite

## Roles


### satellite

This role is the main reason the collection even exists. It is made to allow to completely configure Satellite from the infrastructure part (at least what we need), to individual Content Views and their Publication/Promotions in a simple inventory and execution.

The main point is to have a role that manages the dependencies of object creation/deletion when and how to orchestrate Publications/Promotions of Content Views and manage Activation Keys too.

To simplify things, there is a fixed way to organize the Life Cycle Environments and the group names for the ansible variables is also fixed.

There are only two ansible groups used `test` and `prod` this will translate to two LifeCycle Environments, the name of these LCEs are free, but it will always create the following Promotion path:

1. Library
1. `test` LCE
1. `prod` LCE

The variables this role takes and their explanation are defined in `roles/satellite/vars/main.yml`.

### switch_servers

### update_hosts
