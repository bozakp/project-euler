import time
start = time.time()

a=0
n=1
while a<1000:
	n=n*2
	a=a+1
n=str(n)
sum=0
for x in n:
	sum=sum+int(x)
print "Answer:", sum


elapse = time.time()-start
print "Time(ms):", elapse*1000
