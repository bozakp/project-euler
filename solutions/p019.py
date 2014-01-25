import time
start = time.time()

norm=[31,28,31,30,31,30,31,31,30,31,30,31]
leap=[31,29,31,30,31,30,31,31,30,31,30,31]
d=2
y=1901
n=0
while y<2001:
	if y%4==0:
		for x in leap:
			if d%7==0:
				n=n+1
			d=d+x
	else:
		for x in norm:
			if d%7==0:
				n=n+1
			d=d+x
	y=y+1
print "Answer:", n

elapse = time.time()-start
print "Time(ms):", elapse*1000

