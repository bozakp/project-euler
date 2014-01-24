import time
start = time.time()

import math
t=0
a=1
num=0
while num<500:
	t=t+a
	num=0
	b=math.sqrt(t)
	c=1
	while c<=b:
		if t%c==0:
			num=num+2
		c=c+1
	a=a+1
print "Answer:", t

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")