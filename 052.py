import time
start = time.time()

for x in range(10,17)+range(100,170)+range(1000,1700)+range(10000,17000)+range(100000,170000)+range(1000000,1700000):
	l = list(a for a in str(x))
	l.sort()
	for m in range(2,7):
		n = list(a for a in str(m*x))
		n.sort()
		if n!=l:
			break
	else:
		print "Answer:", x
		break

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")