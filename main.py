#!/usr/bin/python

import random

def gen():
	i = 0
	r = []
	while i < 6:
		s = "".join([random.choice('ABCDE0123456789'),random.choice('ABCDE0123456789')])
		r.append(s)
		i+=1
		r[0]="".join(random.choice('ABCDEF0123456789'),random.choice('ABCDEF0123456789'))
	return ":".join(r)

	a=input("How many? \n > ")
	for j in range (a):
		print gen()