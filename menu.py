#!/usr/bin/env python

import Tkinter as tk
import os
import urllib2
import re
import sys, tty, termios
 
def keycodess(event):
	x = event.char
	if x == "a":
		print "A done"
def list():
	response = urllib2.urlopen('http://www.liquiddota.net/stream')
	html = response.read()
	sr=re.findall(r"stream\/([a-zA-Z0-9_-]{2,20})",html)
	return sr
def bar():
	fd = sys.stdin.fileno()
	# save original terminal settings 
	old_settings = termios.tcgetattr(fd)
	# change terminal settings to raw read
	tty.setraw(sys.stdin.fileno())
	
	ch = sys.stdin.read(1)
	# restore original terminal settings 
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch
def foo():
	mn=""
	idx=0;

	for name in menu:
	 mn+= "[{0}]:{1}".format(idx,name)
	 for i in range(16-len(name)): mn+=" "
	 idx += 1
	 if(idx%3==0): mn+="\n"
	 if idx==10: break
	print mn 
		
	print('enter stream no. :')
	choice=bar()
	nx=ord(choice)-ord('0')
	print "opening stream : {0}".format(menu[nx])
	os.system(cmd+menu[nx]+" "+res)



cmd="livestreamer twitch.tv/"
res="low"

#root=tk.Tk()
#root.bind_all('', keycodess)
#root.mainloop()

menu=list()
foo()
while 1==1:
	print "continue? [0]=no [1]=yes [2]=refresh :"
	opt=bar()
	if(opt=='2'):menu=list();foo()
	elif(opt=='1'):foo() 
	else : break
