# Overview

[![Build Status](https://dev.azure.com/odluser289100/flask-sklearn-app/_apis/build/status%2FArchieHarrodine.Azure-Cloud-DevOps?branchName=main)](https://dev.azure.com/odluser289100/flask-sklearn-app/_build/latest?definitionId=2&branchName=main)

<TODO: complete this with an overview of your project>

## Project Plan
This project is very short and done by a single person, so the project plan doesn't make a lot of sense in some places. Trello boards and time driven spreadsheets make the most sense when there are teams that need an effective way to communicate progress, and when the project is large enough in scope that it isn't following a tutorial for each step. 

* [Spreadsheet](https://docs.google.com/spreadsheets/d/1Gg3DPtGbxHriWF4rwVGyFEUSNVV8iF4S_twSMcztPII/edit?usp=sharing) detailing the project plan.
* [Trello Board](https://trello.com/invite/b/6902011b57350ecc305c87a9/ATTI697d669010881e0e20de03d02c6557ce017E5E7C/azure-cloud-with-devops) used for managing tickets in the project.

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

1. in Azure CLI (bash): ssh-keygen -t rsa; press enter on all
2. cat /home/odl_user/.ssh/id_rsa.pub
3. copy key into github, settings, SSH and GPG keys, add new SSH key
4. go to forked repository, go on code, then SSH, "git@github.com:ArchieHarrodine/Azure-Cloud-DevOps.git"
5. git clone git@github.com:ArchieHarrodine/Azure-Cloud-DevOps.git
6. python -m venv .venv
7. source .venv/bin/activate
8. go into your github folder
9. run az webapp up --name [Your_unique_app_name] --resource-group [resource-group] --sku B1 --logs --runtime "PYTHON:3.10" ; assume that unique name is flask-sklearn-app, resource group is Azuredevops. let it deploy.
10. to test , run in another terminal chmod +x make_predict_azure_app.sh, ./make_predict_azure_app.sh. should return Port: 443
{"prediction":[697.206833661433]}
once built
12. Go to Azure DevOps organisations, view organisations, create organisation, then creare project with app name
13. Go to settings, then service connection, create service connection, Azure resource manager. Use default everything, name it myServiceConnection. grant it access permission to all pipelines
14. Create personal access token (PAT) in top right user settings. call it myPAT and give it full access. copy it as you wont access it again
15. Back to settings, make an Agentpool, myAgentPool, self hosted, grant permission
16. go to virtual machines, create new VM, use ur resource group, name myLinuxVM, availability options: no infrastructure needed. use image DS1_v2, use password authentication. username: devops_admin, AzureDevops@123, allow SSH 22 ports. review + create
17. once deployed, open up another cli. copy the public IP attached ssh devops_admin@public ip, login
18. then:
sudo snap install docker
sudo groupadd docker
sudo usermod -aG docker $USER
19. Go back to myAgentPool, new agent, go to Linux, click download to get the link
20. back on ur app:
curl -O https://download.agent.dev.azure.com/agent/4.261.0/vsts-agent-linux-x64-4.261.0.tar.gz
mkdir myagent && cd myagent
tar zxvf ../vsts-agent-linux-x64-4.261.0.tar.gz
./config.sh
21. then to fill in: do license Y, server url: https://dev.azure.com/organisation name, enter, enter PAT, agentpool name, enter the rest
22. do this
sudo ./svc.sh install
sudo ./svc.sh start
sudo apt-get update
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
sudo apt-get install python3.10-venv
sudo apt-get install python3-pip
sudo apt-get install python3.10-distutils
sudo apt-get -y install zip
sudo apt install pipx
export PATH=$HOME/.local/bin:$PATH
pipx install pylint
23. Check that in the agent tab of myAgentPool that myLinuxVM is an agent there 
24. Go to pipeline, create pipeline, connect with github, select forked repo, select existing pipeline and pick azure-pipelines.yml
25. Run the pipeline, will do the build stage and deploy stage. when it gets to deploy you will need to give permissions. just click permit
26. will now be redeploying the webapp

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


