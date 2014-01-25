import time
start = time.time()

import math
n=[0 for a in range(1001)]
c=5
while c<=500:
	a=c-1
	while a>0.707*c:
		b=math.sqrt(c*c - a*a)
		if b%1==0:
			if a+b+c>1000:
				break
			else:
				b=int(b)
				n[a+b+c]=n[a+b+c]+1
		a=a-1
	c=c+1
e=0
d=0
while e<1001:
	if n[e]>d:
		c=e
		d=n[e]
	e=e+1
print "Answer:", c

elapse = time.time()-start
print "Time(ms):", elapse*1000

