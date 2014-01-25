import time
start = time.time()

a=2
sum=0
while a<360000:
	b=0
	for c in str(a):
		d=int(c)
		b=b+d*d*d*d*d
	if b==a:
		sum=sum+a
	a=a+1
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
