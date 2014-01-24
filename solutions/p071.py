import time
start = time.time()

n=2
d=5
for e in range (8,1000001):
	f=int(e*3/7)
	if e%7==0:
		f=f-1
	if e*n<f*d:
		n,d=f,e

print "Answer:", n

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")