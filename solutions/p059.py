import time
start = time.time()

f=open('C:/Users/Phil/Programming/Project Euler/Labview/Text Files/cipher1.txt', 'r')
lst=f.read().split(',')

lst=list(int(a) for a in lst)

lst2=range(len(lst))

for a in range(97,123):
	for b in range(97,123):
		for c in range(97,123):
			i=0
			while (i<len(lst)):
				lst2[i]=chr(lst[i] ^ a)
				i=i+3
			i=1
			while (i<len(lst)):
				lst2[i]=chr(lst[i] ^ b)
				i=i+3
			i=2
			while (i<len(lst)):
				lst2[i]=chr(lst[i] ^ c)
				i=i+3
			if " the " in "".join(lst2):
				print "Answer:", sum(ord(a) for a in lst2)


elapse = time.time()-start
print "Time(ms):", elapse*1000

