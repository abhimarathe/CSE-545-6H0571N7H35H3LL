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
This script will one command-line argument, the path of the php file. There is a sample phpVuln.py provided to test the following script.
```
$ python phpVulnerabilityFinder.py phpVuln.php
```
### Shellcode Generator
To generate shellcode for x86_32
```
$ g++ -std=c++11 shellcode_generator.cpp -o shellcode_gen
$ ./shellcode_gen
```

### Input Sanitizer
To sanitize user input
```
$ g++ -std=c++11 input_sanitization.cpp -o ip_sanitize
$ ./ip_sanitize
```

### Code Analyzer
To analyze source and binary files
```
$ python CodeAnalyzer.py
```
