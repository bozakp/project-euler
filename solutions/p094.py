import time
start = time.time()

import math
sum=0
for a in range(5,333333333):
	b=math.sqrt(0.75*a*a+0.5*a-0.25)
	c=math.sqrt(0.75*a*a-0.5*a-0.25)
	if b%1==0:
		sum=sum+3*a-1
	if c%1==0:
		sum=sum+3*a+1
	if a%1000000==0:
		print a

print "Answer:", sum


elapse = time.time()-start
print "Time(ms):", elapse*1000
