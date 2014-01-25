import time
start = time.time()

s=set([0,1,2,3,4,5,6,7,8,9])
z=0
for a in s:
	for b in (s-set([a])):
		for c in (s-set([a,b])):
			for d in (s-set([a,b,c])):
				for e in (s-set([a,b,c,d])):
					for f in (s-set([a,b,c,d,e])):
						for g in (s-set([a,b,c,d,e,f])):
							for h in (s-set([a,b,c,d,e,f,g])):
								for i in (s-set([a,b,c,d,e,f,g,h])):
									z=z+1
									if z==1000000:
										print "Answer:", str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(list(s-set([a,b,c,d,e,f,g,h,i]))[0])
										s=set([])

elapse = time.time()-start
print "Time(ms):", elapse*1000
