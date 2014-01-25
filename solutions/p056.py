import time
start = time.time()

max=0
for a in range(70,100):
	for b in range(70,100):
		c=sum(int(x) for x in str(a**b))
		if c>max:
			max=c
print "Answer:", max

elapse = time.time()-start
print "Time(ms):", elapse*1000
