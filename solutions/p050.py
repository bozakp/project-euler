import time
start = time.time()

import math
primes=[2,3]
a=5
while a<70000:
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

def isprime(n):
	a=0
	while n>=primes[a]**2:
		if n%primes[a]==0:
			return False
			break
		a=a+1
	return True

sum=0
n=15
m=0
b=0
c=0
while b<(len(primes)-200):
	while m<n:
		sum=sum+primes[b+m]
		m=m+1
		if sum>1000000:
			b=len(primes)
			break
	while sum<1000000:
		sum=sum+primes[b+m]
		m=m+1
		if isprime(sum):
			n=m
			c=sum
	b=b+1
	sum=0
	m=0
print "Answer:", c



elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")