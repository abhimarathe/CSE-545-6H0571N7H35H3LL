import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename')
parser.add_argument('--instructions')
args = parser.parse_args()
print args
commands = args.instructions.split(',')
print commands

def removeAllRetStatements(data):
	instructions = []
	for line in data:
		if 'ret' not in line:
			instructions.append(line)
	return instructions


def findRopGadgets(file,instructions):
	file = os.popen('objdump -S '+ file+' | grep -B 1 ret','r')
	data = file.read().splitlines()
	data = removeAllRetStatements(data)
	for instr in instructions:
		findGadgets(data,instr)
	
def findGadgets(data,instr):
	print '-----------------------Gadgets with'+ instr+' ----------------------'
	for line in data:
		if instr in line:
			print line
			print '\n'

findRopGadgets(args.filename,args.instructions.split(','))
