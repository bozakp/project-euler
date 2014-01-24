import time
start = time.time()

c=0
for a in range(9182, 10000):
	d=str(a)+str(2*a)
	if set(d)==set("123456789") and int(d)>c and len(d)==9:
		c=int(d)
print "Answer:", c


elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")