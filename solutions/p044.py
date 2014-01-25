import time
start = time.time()

import math
for a in range(1,3000):
	for b in range(a,3000):
		pa=a*(3*a-1)/2
		pb=b*(3*b-1)/2
		if math.sqrt(24*(pa+pb)+1)%3==2 and math.sqrt(24*(pb-pa)+1)%3==2:
			print (pb-pa)

elapse = time.time()-start
print "Time(ms):", elapse*1000

