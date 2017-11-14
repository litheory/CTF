# -*- coding:utf-8 -*-
#明文批量转md5
from hashlib import md5
import string
import re
import random

def genmd5(ming_name,mi_name):
	if ming_name == '':
		ming_name = "mingwen.txt"
	if mi_name == '':
		mi_name = "md5dict.txt"
	mingwen = open(ming_name,"r")
	md5dict = open(mi_name,"w")
	for i in mingwen:
		md5dict.write(md5(i).hexdigest())
		md5dict.write("".join(i))

# md5.digest() //返回: '\x05\xc1*(s48l\x94\x13\x1a\xb8\xaa\x00\xd0\x8a' 
# md5.hexdigest() //返回: '05c12a287334386c94131ab8aa00d08a' 

#  0e46379442318098
if __name__=='__main__':
	ming_name = raw_input("Enter the text you want to md5 encode:\n")
	mi_name = raw_input("Input the save dict name:\n")
	genmd5(ming_name,mi_name)
	print 'ok'