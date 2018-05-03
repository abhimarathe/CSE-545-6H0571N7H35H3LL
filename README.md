# CSE-545-6H0571N7H35H3LL
This repository contains tools we designed for attack and defense CTF.
### Network_analyzer
To run network_analyzer script, run the network_analyzer script. It will generate pcap files.
```
$ ./network_analyzer
```
### Command-line-injection
command-line-injection script will take url, port, command to inject as parameters.
```
$ python command-line-injection.py team1 20003 /bin/sh
```
### Sanitization Wrapper
Sanitization wrapper will take one command-line argument, which is a binary file's path.
```
$ sanitizationWrapper backup-child
```
### ROP Gadget Finder
This script will take two command-line arguments, the path of the binary and the comma separated list of x86 instructions. Please make sure there is no space between the instructions.
```
$ python findRopGadget.py --filename sample_c --instructions mov,pop,xor,inc
```
### PHP Vulnerability Finder
This script will take one command-line argument, the path of the php file. There is a sample phpVuln.py provided to test the following script.
```
$ python phpVulnerabilityFinder.py phpVuln.php
```

