# Local cloud application

<p>
  <img src="https://img.shields.io/badge/Made%20with-Python v3.8-darkgreen?style=flat&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Made%20with-Docker-blue?style=flat&logo=docker&logoColor=white">
</p>

# Table of contents

# About
...

# Installation
This part is dedicated to the prerequisites to launch the application.

## Git [optional]
You can download the project by pressing the ***Code/Download ZIP*** button on GitHub or else you can type the following command in your terminal if you have Git of course.

```
$ git clone https://github.com/rafidini/local-cloud.git
```

## Docker
> **Docker**
:
*Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. - **Wikipedia***

You can download the desktop software by taking a look at this [link](https://www.docker.com/get-started).

In order to use the app you will have to install both ***Docker*** and ***Docker Compose***.

# Usage
Make sure you have downloaded ***Docker*** before beginning. The following instructions are compatible
with linux and macOs terminals.

1. In a terminal, go into the *api* directory :
```bash
$ cd api
```

2. Build a *Docker* image
```bash
$ docker build -t local-cloud .
```

3. Run a *Docker* container
```bash
$ docker run --name cloud local-cloud

Hello, World at 2021-10-05 18:22:09.811861!
```

4. Restart the *Docker* container
```bash
$ docker restart cloud
```

5. Delete the *Docker* container by
   1.  Listing the containers
```bash
$ docker ps -a
CONTAINER ID   IMAGE         COMMAND            CREATED         STATUS                      PORTS     NAMES
6d1c5639e80c   local-cloud   "python main.py"   2 minutes ago   Exited (0) 59 seconds ago             cloud
```
   2.  Delete the container
```bash
$ docker rm 6d1c5639e80c
6d1c5639e80c
```

   3.  List the image(s)
```bash
$ docker images -a
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
local-cloud   latest    4427d0f42533   16 minutes ago   889MB
```

   4.  Delete the image(s)
```bash
$ docker rmi local-cloud
Untagged: local-cloud:latest
Deleted: sha256:4427d0f425337e2bb8716cd0422f1b11fb00da5f8c739f090f190e1ced64373b
```

# Contributing
...

# Help
...

# Credits
...
