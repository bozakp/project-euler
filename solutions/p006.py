import time
start = time.time()

a=0
sum=0
sums=0
while a<100:
	a=a+1
	sum=sum+a
	sums=sums+a*a
print "Answer:", sum*sum-sums

elapse = time.time()-start
print "Time(ms):", elapse*1000

