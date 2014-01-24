import time
start = time.time()

import math
primes=[2,3]
a=5
while a<100000:
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

def is_prime(n):
	a=0
	while n>=primes[a]**2:
		if n%primes[a]==0:
			return False
			break
		a=a+1
	return True

a=4
n=9
t=5
p=3
while 100*p/t>=10:
	if is_prime(n+a):
		p=p+1
	if is_prime(n+2*a):
		p=p+1
	if is_prime(n+3*a):
		p=p+1
	n=n+4*a
	t=t+4
	a=a+2

print "Answer:", math.sqrt(n)

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")