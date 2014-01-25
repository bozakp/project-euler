import time
start = time.time()

z=0
for a in range(0,2):
	for b in range(0, (200-200*a)/100+1):
		for c in range(0, (200-200*a-100*b)/50+1):
			for d in range(0, (200-200*a-100*b-50*c)/20+1):
				for e in range(0, (200-200*a-100*b-50*c-20*d)/10+1):
					for f in range(0, (200-200*a-100*b-50*c-20*d-10*e)/5+1):
						for g in range(0, (200-200*a-100*b-50*c-20*d-10*e-5*f)/2+1):
							z=z+1
print "Answer:", z

elapse = time.time()-start
print "Time(ms):", elapse*1000

