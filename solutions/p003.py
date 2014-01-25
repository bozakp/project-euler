import time
start = time.time()

import math
primes=[2,3]
a=5
c=600851475143
while a<math.sqrt(c):
	for x in primes:
		if a%x==0:
			break
	else:
		primes.append(a)
		if c%a==0:
			c=c/a
	a=a+2
print "Answer:", c

elapse = time.time()-start
print "Time(ms):", elapse*1000

