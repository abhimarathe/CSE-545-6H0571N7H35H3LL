from pwn import *
import sys
import re
def input_sanitization(input_string):
	input_string = re.sub(r"\W",'',input_string)
	return input_string
sh = process(sys.argv[1])
msg1 = sh.recv(timeout=1)
while msg1 != None:
	print msg1
	try:
		input1 = raw_input()
		#input1 = input_sanitization(str(input1))
		#print input1
		sh.sendline(input1)
		msg1 = sh.recv()
		
	except (RuntimeError, TypeError, EOFError):
		print "Exception"
		exit(0)
sh.close()
