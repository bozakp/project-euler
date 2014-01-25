import time
start = time.time()

sum=1
a=1
b=1
while a<=500:
	sum=sum+4*b+20*a
	b=b+8*a
	a=a+1
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
