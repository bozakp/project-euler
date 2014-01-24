import time
start = time.time()

import math
primes=[2,3]
a=5
n=2
while n<10001:
	b=math.sqrt(a)
	for x in primes:
		if a%x==0:
			break
		if x>b:
			primes.append(a)
			n=n+1
			break
	else:
		primes.append(a)
		n=n+1
	a=a+2
print "Answer:", primes[10000]

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")