import time
start = time.time()

import math
a=str(math.factorial(100))
sum=0
for x in a:
	sum=sum+int(x)
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000

