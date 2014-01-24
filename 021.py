import time
start = time.time()

import math
def d(x):
	a=2
	b=math.sqrt(x)
	c=1
	while a<b:
		if x%a==0:
			c=c+a+x/a
		a=a+1
	if b%1==0:
		c=c+b
	return c
sum=0
e=5
while e<10000:
	if d(d(e))==e and d(e)!=e:
		sum=sum+e
	e=e+1
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")