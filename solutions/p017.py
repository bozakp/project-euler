import time
start = time.time()

otn=3+3+5+4+4+3+5+5+4
otnt=otn+3+6+6+8+8+7+7+9+8+8
otnn=otnt+6*10+otn+6*10+otn+5*10+otn+5*10+otn+5*10+otn+7*10+otn+6*10+otn+6*10+otn
hand=otnn+3*99+7*100
sum=otnn+3*100+hand+3*100+hand+5*100+hand+4*100+hand+4*100+hand+3*100+hand+5*100+hand+5*100+hand+4*100+hand+3+8
print "Answer:", sum

elapse = time.time()-start
print "Time(ms):", elapse*1000
