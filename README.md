# CSE-545-6H0571N7H35H3LL
This repository contains tools we designed for attack and defense CTF.
### Network_analyzer
To run network_analyzer script, run the network_analyzer script. It will generate pcap files.
```
$ network_analyzer
```
### Command-line-injection
command-line-injection script will take url, port, command to inject as parameters.
```
$ command-line-injection.py team1 20003 /bin/sh
```
### Sanitization Wrapper
Sanitization wrapper will take one command-line argument, which is a binary file's path.
```
$ sanitizationWrapper backup-child
```
