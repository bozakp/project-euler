import time
start = time.time()

import math
primes=[2,3]
a=5
while a<10000:
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
		a=a+1
	return True
num=0
a=11
sum=0
while num<11:
	if int(str(a)[0]) in [2,3,5,7] and int(str(a)[-1]) in [3,5,7] and  not any(True for y in str(a)[1:] if y in [2,4,6,8,0]):
		for b in range(len(str(a))):
			if b==0:
				if not isprime(a):
					break
			else:
				if (not isprime(int(str(a)[b:]))) or (not isprime(int(str(a)[:-b]))):
					break
		else:
			sum=sum+a
			num=num+1
	a=a+2
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000

