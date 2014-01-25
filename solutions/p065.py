import time
start = time.time()

d=[]
c=range(1,34)
c.reverse()
for a in c:
	d.append(1)
	d.append(2*a)
	d.append(1)

d.remove(1)

num=1
den=1
for x in d:
	num, den = den, (den*x+num)

print "Answer:", sum(int(n) for n in str(num+2*den))


elapse = time.time()-start
print "Time(ms):", elapse*1000

