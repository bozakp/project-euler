import time
start = time.time()

import math
a=3
sum=0
while a<2000000:
	b=0
	for c in str(a):
		b=b+math.factorial(int(c))
	if b==a:
		sum=sum+a
	a=a+1
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")