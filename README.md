# DSOR 651 Examples

This repository contains examples for DSOR 651. These examples are designed be executed on the AceHub compute cluster. To run these examples:

1. Ensure you have a CDN account
2. Ensure you are connected to the CDN Network (VPN is required if you don't have a wired connection)
3. Ensure you have a git.antcenter.net user account
4. Create and configure your git.antcenter.net personal account token with the AceHub configuration
 - Go to your git.antcenter.net [User Profile Personal Access Tokens](https://git.antcenter.net/-/user_settings/personal_access_tokens)
 - Add new token with read_repository access (AceHub needs to be able to pull containers to execute from the git.antcenter.net container registry)
 - Copy this token
 - Enter this token as the IPS Password on the following [AceHub User Configuration Page](https://hub.rangers.nhl.antcenter.net/userconfig)
 - Enter the git.antcenter.net:4567 as the registry
 - Enter you git.antcenter.net username as the IPS Username
 - Enter a name and press Save
5. Click [here](https://hub.rangers.nhl.antcenter.net/environments) and enter the following as the image namge git.antcenter.net:4567/nranly/dsor-651-containers:latest
 to create a new development.
 - Configure as needed
 - Press Launch
6. Your created and running environments are shown [here](https://hub.rangers.nhl.antcenter.net/environments).
 - Once your environment is "Ready", expand the environment and click "Open-UI"

## multiprocessing

## mpi4py