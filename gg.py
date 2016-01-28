#!/usr/bin/env python

import Tkinter
from Tkinter import *
import os
import tkMessageBox
import urllib2
import re
def list():
	sr=re.findall(r"stream\/([a-zA-Z0-9_]{2,20})",html)
	vw=re.findall(r"stream\/([a-zA-Z0-9_]{2,20})[\s\S]+?\>([0-9]{1,10})\<\/td\>",html)
	lines  = html.split('\n')
	for line in lines:
		if(re.search(r"(rightmenu)",line)):
			v=re.findall(r"=\"([\S]{2,20}), ([0-9]{2,10}) viewers.+\/stream\/([\S]{2,20})\"",line)
			print v	
	return v

cmd="livestreamer twitch.tv/"
res="low"

def strim(x):
	os.system(cmd+x+" "+res)
	#tkMessageBox.showinfo( "ad", x)

def run():
	#strim(st+E1.get())
	os.system(cmd+E1.get())

def menu():
	menu = []
	idx=0
	menux=''
	count=0
	colorx='#7DDD2A'
	for name in list():
		if(count==0):colorx='#E60D0D'
		if(count==1):colorx='#FF4500'
		if(count==2):colorx='#FF7F50'
		if(count==3):colorx='#DAA520'
		if(count==4):colorx='#ADFF2F'
		if(count >=5 and count<10):colorx='#BFDD2A'
		if count < 30:
			B = Tkinter.Button(xbox, text = name[2]+'<br>'+name[1]+'<br>'+name[0],
					bg=colorx,
					command =lambda x=name[2]:
					strim(x), width=10,height=5)
			B.grid(row=idx/5,column=idx%5)
			idx += 1
			count+=1




response = urllib2.urlopen('http://www.liquiddota.net/stream')
html = response.read()
	






top = Tkinter.Tk()
top.geometry("700x500")
top["bg"]="#FFFFF5"
top.attributes('-alpha', 0.3)
# Code to add widgets will go here...
E1 = Entry(top, bd =5)
E1.pack()
B1 = Button(top, width=5,height=1, text='GO', command=run)
B1.pack()


xbox = Tkinter.Frame(top,height=70,width=100,bg="#FFFFF5")
xbox.pack()
menu()
top.mainloop()
