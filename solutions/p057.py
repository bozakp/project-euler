import time
start = time.time()

num = 0
for a in range(1001):
	n=1
	d=2
	for x in range(a):
		n,d = d,(2*d+n)
	n=n+d
	if len(str(n))>len(str(d)):
		num=num+1

print "Answer:", num

elapse = time.time()-start
print "Time(ms):", elapse*1000
