import time
start = time.time()

f=open('../Labview/Text Files/names.txt', 'r')
e=f.read().split(',')
a=0
for x in e:
	e[a]=x[1:-1]
	a=a+1
e.sort()
sum=0
a=1
for x in e:
	w=0
	for y in x:
		w=w+ord(y)-64
	sum=sum+w*a
	a=a+1
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
