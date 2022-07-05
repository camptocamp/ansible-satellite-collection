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

#### Usable Tags

The role is all-in-one management of satellite. Actions to be performed by the role are defined using a tag in the role. To avoid mis-usages, if no tag is specified, no action is performed.

The tags are defined as follows:

1. define: *Not Idempotent!* will create the environment from scratch. Synchronization of the repos and publishing of ContentViews is performed, due to dependencies in Satellite.
1. change: Will modify the definitions in Satellite, this is idempotent.
1. sync: Will start synchronization of all repositories and wait for them to finish.
1. publish: Will publish all contentviews and composite contentviews defined in the inventory.
1. update-test: Will publish the ContentView, promote it to the testing lifecycle environment, and perform the update of the test machines.
1. update-prod: Will promote the ContentView from testing to production lifecycle environment and perform the update of the prod machines.
1. deprovision: Will remove all the definitions of the satellite objects. Note that ContentViews cannot be automatically de-promoted, so you need to log into the interface and remove the content view from the LifeCycle Environments. Note also that the Repositories are not deleted (because they could be used elsewhere).

#### Variables

Some mandatory variables must be set for the role to work as expected:

- `satellite_url`: The url to access the satellite server
- `satellite_user`: The username used to log into the satellite server, must have enought rights to perform the actions needed by the role
- `satellite_pwd`: The password of the user used to log into the satellite server

### switch_servers

This role will go over machines it is applied to and reconfigure the subscription and package download urls using an activation key.

#### Variables

Some mandatory variables must be set for the role to work as expected see the `role/switch_servers/vars/main.yml` file for their definitions.

### update_hosts

This role allows to update the machines automatically, allowing to hook the process.

#### Update Hooks

It is possible to add hooks to the update process by setting variables:

- `pre_update_hook` allow to execute tasks before the `yum update`
- `post_update_hook` allow to execute tasks after the `yum upadte`
- `perform_yum_update` a boolean controlling the execution of the `yum update` the value is `false` by default


## Releasing

The collection is automatically built by gitlab-ci, to release a new version just tag it with the new version number. For example: `1.0.3` and it will be built and pushed into the gitlab artifacts storage.
