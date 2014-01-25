import time
start = time.time()

import math
f=open('../Labview/Text Files/base_exp.txt', 'r')
grid=f.read().split('\n')
a=0
for x in grid:
	grid[a]=x.split(',')
	b=0
	for y in grid[a]:
		grid[a][b]=int(y)
		b=b+1
	a=a+1

a=1
b=0
for x in grid:
	c=x[1]*math.log10(x[0])
	if c>b:
		b=c
		l=a
	a=a+1
print "Answer:", l

elapse = time.time()-start
print "Time(ms):", elapse*1000
