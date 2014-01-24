import time
start = time.time()

import math
primes=[2,3]
a=5
while a<50000:
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
def isprime(z):
	for x in primes:
		if x==z:
			return True
			break
	else:
		return False
a=-999
d=0
c=0
while a<1000:
	b=0
	while primes[b]<1000:
		if primes[b]>-a and primes[b]>(1-40*(a+40)):
			n=0
			while isprime(n*(n+a)+primes[b]):
				n=n+1
			if n>c:
				d=a*primes[b]
				c=n
		b=b+1
	a=a+1
print "Answer:", d, c

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")