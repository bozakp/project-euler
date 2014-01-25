import time
start = time.time()

import math
primes=[2,3]
a=5
while a<2000000:
	b=math.sqrt(a)
	for x in primes:
		if a%x==0:
			break
		if x>b:
			primes.append(a)
			break
	else:
		primes.append(a)
	a=a+2
sum=0
for x in primes:
	sum=sum+x
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000

