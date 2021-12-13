# Project 2: Scratchcard generator

![Project Image](project-image-url)

> QA DevOps Practical Project

---

### Table of Contents

- [Introduction](#introduction)
- [My Approach](#my-approach)
- [Summary](#summary)
- [ERD](#erd)
- [Jira](#jira)
- [Risk Assessment](#risk-assessment)
- [Service Infrastructure](#service-infrastructure)
- [CI Pipeline](#ci-pipeline)
- [Google Cloud Platform](#google-cloud-platform)
- [Jenkins Build](#jenkins-build)
- [Testing](#testing)
- [Ansible](#ansible)
- [Docker & Docker Compose for services](#docker-&-docker-compose-for-services)
- [Docker Swarm](#docker-swarm)
- [NGINX](#nginx)
- [Demonstration](#demonstration)
- [Webhook](#webhook)
- [Branch](#branch)


---

## Introduction

The purpose of this ReadMe document is to outline the project specification of the DevOps practical project I will be working. This project will involve concepts which include:

-Software Development with Python
-Continuous Integration
-Cloud Fundamentals

#### Architecture

The objective of the project was: "to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together."

This project is primarily concerned with deploying the application.

For this project, I should have:
-Kanban Board: Jira 
-Version Control: GIT & GITHUB
-CI Server: Jenkins
-Configuration Management: Ansible
-Cloud Server: Google Cloud Platform (GCP) Virtual Machines
-Containerisation: Docker
-Orchestration Tool: Docker Swarm
-Reverse Proxy: NGINX

[Back To The Top](#scratchcard-generator)

---

## My Approach

I have decided to make a scratchcard prize generator web application. The application should :
- Use Service1 as Front End
- Use Service2 & Service3 to generate a random number-letter combination; Service2 involves generating number and Service3 involves generating letter
- Use Service4 to generate a prize reward.

[Back To The Top](#scratchcard-generator)

---

## Summary

Once the web application was made and tested in a virual machine , I added a Dockerfile into each of the services to containerise them and made a docker-compose.yaml. Then I made ansible files that involves Inventory, playbook.yaml and roles/tasks. These files can help install docker on the swarm nodes and then set up a docker swarm. After setting these up, I then created a Jenkinsfile with scripts so that jenkin can use these requirements to make a pipeline.

I need 3 new Virtual Machines in Google Cloud Platform and these are:
-jenkins
-manager
-worker

Firstly, I started off by installing Jenkins on the "jenkins" Virtual Machine. As soon as this was complete and installed, I gave jenkins sudo permissions by using the command: "sudo visudo" and as the jenkin user, I have installed docker and docker-compose. I also needed to generate keys as jenkin user by using: "ssh-keygen -t rsa". 

On the "jenkins" Virtual Machine, I placed the generated public key from jenkin user into the manager and worker VMs. Once I have created those two virtual machines ("manager" & "worker"), I used the "jenkins" virtual machine to "ssh" into them.

 Still as the jenkins user, I put the docker login to provide my dockerhub username and password. After providing those credentials, through the jenkins app on port 8080, I installed a webhook for my git repository and enabled it on git, this allows for a rolling update.

[Back To The Top](#scratchcard-generator)

---
## ERD


[Back To The Top](#scratchcard-generator)

---
## Jira

[Back To The Top](#scratchcard-generator)

---
## Risk Assessment


[Back To The Top](#scratchcard-generator)

---
## Service Infrastructure


[Back To The Top](#scratchcard-generator)

---
## CI Pipeline


[Back To The Top](#scratchcard-generator)

---
## Google Cloud Platform
When starting my project, I had to create & test whether my application works by installing a Virtual Machine on Google Cloud Platform. Google Cloud Platform offers services for compute, storage, networking, big data, machine learning and the internet of things(IoT) as well as cloud management, security and developer tools.

In order for me to connect my application to the VM, I had to place my local machines public key in. Then I SSH through VSC to my VM and clone this to GIT repository. By doing this, I have created services for my project.

Once all my services are completed and the application is working successfully, I had to push to GitHub main branch. After the completion, I created 3 VMs for the next stage which are jenkins, manager and worker.

[Back To The Top](#scratchcard-generator)

---
## Jenkins Build

#### Permissions
The next stage is to create a jenkins GCP virtual machine. After creating this, I had to first install and unlock Jenkins. Once these steps are done, I used the command: "sudo visudo" in the jenkins VM to add jenkins to be a sudo user. 

#### Docker & Docker-compose
As the jenkins user, I had to install docker and docker-compose adding the jenkin user to the docker user group. This allows jenkins to use docker without sudo commands and then restarted the terminal.

#### Generating keys
After previous stages, I had to create keys by adding: "ssh-keygen -r rsa" and then using "cat ./.ssh/id_rsa.pub" to get the jenkins public key. 

#### Key signature procedure
As soon as I got the public key, I made 2 GCP VMs which are a manager and a worker. In order for jenkins work on both VMs, I had to place the public key for jenkins into both of the VMs. After this, I had to SSH into both manager and worker VMs through my jenkins machine to generate a key signature.

#### Jenkins Pipeline
After setting previous stages up, I had to make a Jenkins pipeline in order for jenkins to read. This can be done by creating a Jenkinsfile. The pipeline has a number of benefits and in this project, the main benefit is that it has made the process code easier for iterative development with other features such as code review and access control. The Jenkinsfile defines stages and we can give the steps for each stage. 

For this project, I had to execute scripts in my steps as it is easy to implement. Here is a picture of my jenkins pipeline:

![Project Image](project-image-url)



[Back To The Top](#scratchcard-generator)

---
## Testing

Testing is the first stage of a deployment and I had to pytest each service by using --cov ./application after making a venv and installing pytest.

Here is the picture of the pytest.

![Project Image](project-image-url)


[Back To The Top](#scratchcard-generator)

---
## Ansible
Ansible is a tool that generates written instructions for automating IT professionals' work throughout the entire system infrastructure. It is used for application deployment, configuration management, intra-service orchestration and practically anything else a system admin does on a weekly or daily basis. Ansible connects to node on a network and sends Ansible module to each node. It runs these modules through SHH and deletes them once they are done.

So using ansible is the second stage for this project. It is used to automate the connectivity of a manager and its workers. The stages for this to work works as follows:

#### Inventory file
First, I had to create an inventory file in my main directory and used to define which VMs is a manager and which are workers. "StrictHostKeyChecking=no" is the command that is used in inventory file in order for jenkins to run ansible without getting errors.

#### Playbook.yaml
Playbook.yaml is a file that defines which hosts (mentioned in the inventory) will have what roles. 

#### Roles directories
After assigning which hosts will have what roles, I had to make a role directory and directories with the same name as the roles which is mentioned in the playbook.yaml. In each roles, we had to add a new directory called tasks and each of the respective task directories, I had to make a main.yaml. This file needs to be same as the playbooks.

#### main.yaml
In this file, I had to specify the tasks for any node who is assigned to do a task. For an instance, my docker role gets both nodes to install docker and perform the neccessary actions. The master role tells my manager node to set up a docker swarm and export the token, and the worker role tells my worker to join the swarm with the token.

![Project Image](project-image-url)


[Back To The Top](#scratchcard-generator)

---
## Docker & Docker Compose for services
Docker is a container management software so you have containers, images and volumes. The benefits using this software is its simplicity,collaboration,flexibility and totality.

So in order to use this software, I had to make Dockerfiles for each service in order to build images of them. This exposes Services1, Service2, Service3 & Service4 to their ports respectively(5000,5001,5002 &5003).

After making dockerfiles, we need to make a docker-compose.yaml which makes the use of configuration files to build all of the containers at once. It builds and deploys them as 1 service. 


[Back To The Top](#scratchcard-generator)

---
## Docker Swarm
Docker Swarm allows the user to manage multiple containers deployed across multiple host machines.

For this project, I had to SSH into my swarm manager using "StrictHostKeyChecking=no" and pulls the latest images for my services. This also clones and moves into a directory. 

After doing this, I had to docker stack across the swarm using docker-compose.yaml and giving my stack the name randprize


[Back To The Top](#scratchcard-generator)

---
## NGINX
NGINX is a open source software for web serving, reverse proxying, caching and load balancing.

On GCP, I had to create a NGINX VM on GCP and create a nginx.conf. In this VM, I also had to install docker and use the docker run as a NGINX container. NGINX for this project acts as a load balancer and evenly distributes traffic between the manager and worker node.

![Project Image](project-image-url)



[Back To The Top](#scratchcard-generator)

---
## Demonstration

[Back To The Top](#scratchcard-generator)

---
## Webhook
Webhook is used to perform a rolling update. In order to set up this, I had to set it on Jenkins and then on GitHub by using the jenkins ip.

![Project Image](project-image-url)

Now that everything is set up, I am able to push anytime to the repository, This is because Jenkins automatically builds and deploys the new version.

[Back To The Top](#scratchcard-generator)

---
## Branch


[Back To The Top](#scratchcard-generator)