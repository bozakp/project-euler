import time
start = time.time()

import math

n=1000000000000
while 1:
	c=(n*n-n)/2
	if (int(math.sqrt(4*c+1)))%2==1:
		print "Answer:", (int(math.sqrt(4*c+1))+1)/2
		break
	n=n+1


elapse = time.time()-start
print "Time(ms):", elapse*1000

