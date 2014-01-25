import time
start = time.time()

def lenOfDec(n):
	a=20
	b=1
	while ((10**(a+b)/n)%(10**b))!=((10**(a+2*b)/n)%(10**b)):
		b=b+1
	return b

max=0
for a in range(5,1000):
	b=lenOfDec(a)
	if b>max:
		max=b
		c=a

print "Answer:", c

elapse = time.time()-start
print "Time(ms):", elapse*1000

