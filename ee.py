#!/usr/bin/env python

import os
import re

st = ""
#for fx in os.listdir(r'/home/x2/N'):
#	# if file.endswith(".txt"):
#	# print(file)
#	st = st + fx + '<br>'
#	#print file
#	
#for fx in os.listdir(r'/home/x2/S'):
#	# if file.endswith(".txt"):
#	# print(file)
#	st = st + fx + '<br>'
#	#print file
	
fo = open("ht", "r")
ht = fo.read();

#ht.join([ht+st+"</div></body></html>"])
#ht=ht+st+'</div></body></html>'
#fw = open("xs.html", "w")
#fw.write(ht)	

#os.system("google-chrome xs.html")
#print ht

print ht[1]

sr=re.findall(r"\<p\>([\S\s]+?)\<\/p\>",ht)
print sr
