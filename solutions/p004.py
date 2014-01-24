import time
start = time.time()

a=100
b=100
d=0
while a<1000:
	while b<a:
		c=str(a*b)
		if c[0]==c[-1] and c[1]==c[-2] and c[2]==c[-3]:
			if a*b>d:
				d=a*b
		b=b+1
	b=100
	a=a+1
print "Answer:", d

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")