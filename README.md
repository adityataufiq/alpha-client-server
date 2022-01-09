# Alpha Client Server 
Simple Client-Server App Created with Python, and Bash.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## Technologies
Project is created with:
* Python
* Bash
* Socket Module
* Threading Module
* Sys Module

## Setup
To run this project automatically (using job bash file):

```
$ chmod u+x job.sh
$ ./job.sh
```

To run this project manually (if something wrong happen):

```
$ python3 server.py <port>
```

Then, using another terminal (<port> must be same with server, also you can naming <node> freely and run it repeatedly):

```
$ python3 client.py <port> <node>
```