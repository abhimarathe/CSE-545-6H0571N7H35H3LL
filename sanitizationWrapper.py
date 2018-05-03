from pwn import *
import sys
import re
def input_sanitization(input_string):
	if re.compile("[; | \| | \& | \$]", input_string):
		return " "
	else:
		return input_string
sh = process(sys.argv[1])
msg1 = sh.recv(timeout=1)
while msg1 != None:
	print msg1
	try:
		input1 = raw_input()
		#input1 = input_sanitization(str(input1))
		print input1
		sh.send(input1+"\n")
		msg1 = sh.recv()
	except (RuntimeError):
		print "Exception"
		exit(0)
sh.close()
