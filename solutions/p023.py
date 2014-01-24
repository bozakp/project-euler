import time
start = time.time()

import math
def d(x):
	a=2
	b=math.sqrt(x)
	c=1
	while a<b:
		if x%a==0:
			c=c+a+x/a
		a=a+1
	if b%1==0:
		c=c+b
	return c
abn=[]
a=10
while a<28500:
	if d(a)>a:
		abn.append(a)
	a=a+1
a=0
n=[0]
while a<28500:
	n.append(1)
	a=a+1
a=0
while a<len(abn):
	b=0
	while b<=a:
		if abn[a]+abn[b]<len(n):
			n[abn[a]+abn[b]]=0
		b=b+1
	a=a+1
a=0
sum=0
while a<len(n):
	if n[a]==1:
		sum=sum+a
	a=a+1
print "Answer:", sum


elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")