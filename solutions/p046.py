import time
start = time.time()

import math
primes=[2,3]
a=5
d=0
while d==0:
	b=math.sqrt(a)
	for x in primes:
		if a%x==0:
			for c in primes:
				if math.sqrt((a-c)/2)%1==0:
					break
			else:
				print "Answer:", a
				d=1
			break
		if x>b:
			primes.append(a)
			break
	else:
		primes.append(a)
	a=a+2

elapse = time.time()-start
print "Time(ms):", elapse*1000

