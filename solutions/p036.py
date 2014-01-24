import time
start = time.time()

a=1
sum=0
while a<1000000:
	if str(a)==str(a)[::-1] and bin(a)[2:]==bin(a)[2:][::-1]:
		sum=sum+a
	a=a+1
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")