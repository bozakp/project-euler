import time
start = time.time()

n=28433
for x in range(7830457):
	n=2*n%100000000000
n=n+1
print "Answer:", n%10000000000

elapse = time.time()-start
print "Time(ms):", elapse*1000

