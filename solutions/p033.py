import time
start = time.time()

def gcf(x,y):
	if x<y:
		x,y=y,x
	a=y
	while a>0:
		if y%a==0 and x%a==0:
			break
		a=a-1
	return a
a=12
c=1
d=1
while a<100:
	b=11
	while b<a:
		a0=int(str(a)[0])
		a1=int(str(a)[1])
		b0=int(str(b)[0])
		b1=int(str(b)[1])
		if a1!=0 and ((a*b0==b*a0 and b1==a1) or (a*b1==b*a0 and b0==a1) or (a*b0==b*a1 and b1==a0) or (a*b1==b*a1 and b0==a0)):
			c=c*a
			d=d*b
		b=b+1
	a=a+1
c=c/gcf(c,d)
print "Answer:", c

elapse = time.time()-start
print "Time(ms):", elapse*1000
