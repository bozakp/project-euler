import time
start = time.time()

import math
a=1
b=1
while a<500:
	while b<a:
		c=math.sqrt(a*a+b*b)
		if c%1==0 and a+b+c==1000:
			print "Answer:", a*b*c
		b=b+1
	b=1
	a=a+1

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")