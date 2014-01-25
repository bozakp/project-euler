import time
start = time.time()

num=0
for x in range(5,10000):
	c=x
	for y in range(50):
		c=c+int(str(c)[::-1])
		if str(c)==str(c)[::-1]:
			break
	else:
		num=num+1
print "Answer:", num

elapse = time.time()-start
print "Time(ms):", elapse*1000
