import time
start = time.time()

f=open('../Labview/Text Files/words.txt', 'r')
e=f.read().split(',')
a=0
for x in e:
	e[a]=x[1:-1]
	a=a+1
a=0
t=[]
while a<500:
	t.append((a+1)*a/2)
	a=a+1
n=0
for x in e:
	w=0
	for y in x:
		w=w+ord(y)-64
	if t.count(w)>0:
		n=n+1
print "Answer:", n

elapse = time.time()-start
print "Time(ms):", elapse*1000

