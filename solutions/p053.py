import time
start = time.time()

import math
sum=0
for n in range(23,101):
	r=1
	while math.factorial(n)/math.factorial(r)/math.factorial(n-r)<1000000:
		r=r+1
	o=2*(int(n/2)+1-r)
	if n%2==0:
		o=o-1
	sum=sum+o
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
