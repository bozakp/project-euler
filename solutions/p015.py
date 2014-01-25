import time
start = time.time()

import math
b=20
n=math.factorial(b*2)
n=n/math.factorial(b)
n=n/math.factorial(b)
print "Answer:", n

elapse = time.time()-start
print "Time(ms):", elapse*1000
