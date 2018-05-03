#include <iostream>
#include <sstream>
#include <string>

std::string sanitize_input(std::string input) {
	
	if(input.find(";") != std::string::npos) {
		return input.substr(0, input.find(";"));
	}
	else if((input.find("|")!= std::string::npos)||
			(input.find("&")!= std::string::npos)||
			(input.find("$")!= std::string::npos)||
			(input.find("ln -s")!= std::string::npos)||
			(input.find("system")!= std::string::npos)||
			(input.find("execve")!= std::string::npos)||
			(input.find("chroot")!= std::string::npos)||
			(input.find("90")!= std::string::npos)||
			(input.find("fork")!= std::string::npos)||
			(input.find("find")!= std::string::npos)||
			(input.find("printf")!= std::string::npos)||
			(input.find("execlp")!= std::string::npos)) {
				return "";
			}
	return input;
}

int main(int argc, char*argv[]) {
	std::cout << sanitize_input(argv[1]) << std::endl;
	return 0;
}
