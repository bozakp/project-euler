import time
start = time.time()

import math
a=144
while True:
	c=a*(2*a-1)
	if math.sqrt(24*c+1)%3==2:
		if math.sqrt(8*c+1)%2==1:
			print "Answer:", c
			break
	a=a+1

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")