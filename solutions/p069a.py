import time
start = time.time()

import math
primes=[2,3]
a=5
while a<1000000:
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

fact=[]
for f in range(999999):
	fact.append(set(pfact(f+2)))

print fact[:10]

c=float(3)
d=6
for x in range(11,1000001):
	n=1
	s=fact[x-2]
	for y in range(x-2):
		if fact[y]&s!=set([]):
			n=n+1
			if c*n>x:
				break
	else:
		if x/n>c:
			c=float(x/n)
			d=x
	if x%1000==0:
		print x
print "Answer:", d


elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")