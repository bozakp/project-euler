import time
start = time.time()

a=2
s=set([])
while a<100:
	b=a+1
	while len(str(b*a)+str(a)+str(b))<10:
		if set(str(a)+str(b)+str(a*b))==set("123456789"):
			s=s|set([a*b])
		b=b+1
	a=a+1
print "Answer:", sum(x for x in s)

elapse = time.time()-start
print "Time(ms):", elapse*1000
