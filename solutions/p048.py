import time
start = time.time()

a=1
sum=0
while a<=1000:
	sum=sum+pow(a,a,10000000000)
	a=a+1
print "Answer:", int(str(sum)[-10:])

elapse = time.time()-start
print "Time(ms):", elapse*1000
