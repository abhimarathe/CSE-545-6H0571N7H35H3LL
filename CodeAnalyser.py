import re
import os
import sys

vulnerableFunctions = ['strcpy','gets','puts','scanf','printf','fopen','fputs','system','execve','access']

def findFunctionsInBinary(file):
	funcAddr = {}
	file = os.popen('objdump -R '+file,'r')
	data = file.readline()
	while 'OFFSET' not in data.split():
		data = file.readline()
	while data != '':
		data = file.readline()
		tokens = data.split()
		if len(tokens) == 3:
			func = tokens[2].partition('@')[0]
		if func in vulnerableFunctions:
			funcAddr[tokens[0][1:]] = func
	return funcAddr

def findVulnerableFunctionCalls(file):
	file = os.popen('objdump -S '+file,'r')
	data = file.readline()
	print data
	while '.text:' not in data.split():
		data = file.readline()

	while data != '':
		data = file.readline()
		tokens = data.split()
		if 'call' in tokens and tokens.index('call') + 2 < len(tokens):
			func = tokens[tokens.index('call') + 2][1:].partition('@')[0]
			if func in vulnerableFunctions:
				print func + ' call at address ' + tokens[0][:-1]




def findVulnerablefunction(line,num):
	for func in vulnerableFunctions:
		pattern = re.compile(func)
		if re.search(pattern,func) != None:
			print "Found " + func + " on line number " + str(num) 

funcAddr = findFunctionsInBinary(sys.argv[1])
print funcAddr
findVulnerableFunctionCalls(sys.argv[1])




