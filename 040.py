import time
start = time.time()

a=1
s="0"
while len(s)<1000002:
	s=s+str(a)
	a=a+1
ans=int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000])
print "Answer:", ans

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")