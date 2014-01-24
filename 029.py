import time
start = time.time()

s=set([])
for a in range(2,101):
	for b in range(2,101):
		s=s|set([pow(a,b)])
print "Answer:", len(s)

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")