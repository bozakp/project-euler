import time
start = time.time()

num=0
max=8
for d in range(2,max+1):
	num = num + (1 if d<=4 else 0)*(d-1)
	print "d:", d, "    num:", num

print "Answer:", num

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")