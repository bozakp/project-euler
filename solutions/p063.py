import time
start = time.time()

print "Answer:", sum(1 if n==len(str(a**n)) else 0 for n in range(1,22) for a in range(1,10))




elapse = time.time()-start
print "Time(ms):", elapse*1000
