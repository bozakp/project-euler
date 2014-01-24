import time
start = time.time()

corr = {"0":0, "1":1, "2":4, "3":9, "4":16, "5":25, "6":36, "7":49, "8":64, "9":81}

z=range(601)
for a in range(1,601):
	b=a
	while (b!=89 and b!=1):
		b=sum(corr[c] for c in str(b))
	if b==89:
		z[a]=1
	else:
		z[a]=0

sum=sum(d for d in z)

for a in range(601,10000000):
	b=0
	for c in str(a):
		b=b+corr[c]
	sum = sum + z[b]

print "Answer:", sum


elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")