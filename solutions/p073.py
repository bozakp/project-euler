import time
start = time.time()

import math
primes=[2,3]
a=5
while a<115:
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

def pfact(n):
	p=[]
	a=0
	while n>=primes[a]**2:
		if n%primes[a]==0:
			p.append(primes[a])
			while n%primes[a]==0:
				n=n/primes[a]
		a=a+1
	if n!=1:
		p.append(n)
	return p

n=0
for x in range(5,12001):
	if x%100==0:
		print x
	a=x/3
	b=x/2
	if x%3!=0:
		a=a+1
	if x%2!=0:
		b=b+1
	s=pfact(x)
	if len(s)==1:
		n=n+b-a
	else:
		n=n+sum(1 for y in range(a,b) if not any(True for z in s if y%z==0))

print "Answer:", n



elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")