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
5. Click [Create New Environment](https://hub.rangers.nhl.antcenter.net/environments) and enter the following as the image name **git.antcenter.net:4567/nranly/dsor-651-containers:latest**
 to create a new development.
  - Configure as needed
  - Press Launch or Save to add this environment configuration to be used for later
6. Your created and running environments are shown [here](https://hub.rangers.nhl.antcenter.net/environments).
  - Once your environment is "Ready", expand the environment and click "Open-UI"
  - If it appears your environment is stuck, mouse-over the information icon next to the pending text in the user interface; if an error occured, this pop-up will show the error and can be used to debug the cause 
7. The development environment is based on Visual Studio Code (VS Code); you can use VS Code in many ways as you would on your local laptop. Note the following important details:
  - All files and folders are within the development environment, not your local system
  - Any files or folders created that are not within the /remote_home/ folder are lost after the environment stops running
  - Save any files you would like to use in a different development environment session or keep to the /remote_home/ folder or to a git service such as git.antcenter.net. 
  - "Open Folder" to get started.  If you need to create a folder, first open the existing parent folder and create child folders as needed through the VS Code Explorer side-panel. You can right-click and create Folders and Files as needed. You can also clone a git repo to get started.

## multiprocessing

## mpi4py