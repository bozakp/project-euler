import time
start = time.time()

a=1
c=2
d=1
while len(str(d))<1000:
	d, a = a+d, d
	c=c+1
print "Answer:", c

elapse = time.time()-start
print "Time(ms):", elapse*1000
