import time
start = time.time()

a=0
b=1
c=0
sum=0
while c<4000000:
	c=a+b
	if c%2==0:
		sum=sum+c
	a=b
	b=c
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")