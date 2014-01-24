import time
start = time.time()

s=set([0,1,2,3,4,5,6,7,8,9])
sum=0
for a in s:
	for b in (s-set([a])):
		for c in (s-set([a,b])):
			for d in (s-set([a,b,c])):
				for e in (s-set([a,b,c,d])):
					for f in (s-set([a,b,c,d,e])):
						for g in (s-set([a,b,c,d,e,f])):
							for h in (s-set([a,b,c,d,e,f,g])):
								for i in (s-set([a,b,c,d,e,f,g,h])):
									if int(str(b)+str(c)+str(d))%2==0 and int(str(c)+str(d)+str(e))%3==0 and int(str(d)+str(e)+str(f))%5==0 and int(str(e)+str(f)+str(g))%7==0 and int(str(f)+str(g)+str(h))%11==0 and int(str(g)+str(h)+str(i))%13==0 and int(str(h)+str(i)+str(list(s-set([a,b,c,d,e,f,g,h,i]))[0]))%17==0:
										sum = sum + int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(list(s-set([a,b,c,d,e,f,g,h,i]))[0]))
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")