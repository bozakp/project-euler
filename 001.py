import time
start = time.time()

a=3
sum=0
while a<1000:
	sum=sum+a
	a=a+3
a=5
while a<1000:
	sum=sum+a
	a=a+5
a=15
while a<1000:
	sum=sum-a
	a=a+15
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")