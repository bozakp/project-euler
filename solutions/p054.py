import time
start = time.time()


tonum={'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def score_hand(x):
	z=x.split()
	d=z[0][1]
	for f in z:
		if d!=f[1]:
			flush=False
			break
	else:
		flush=True
	h=[]
	for y in z:
		h.append(tonum[y[0]])
	h.sort()
	if is_straight(h):
		if flush:
			score=9+0.01*h[4]
		else:
			score=5+0.01*h[4]
	elif flush:
		score=5+0.01*h[4]
	else:
		s = set(h)
		if len(s)!=5:
			if len(s)==2:
				b=list(s-set([h[2]]))[0]
				if h.count(h[2])==3:
					score=7+0.01*h[2]+0.0001*b
				if h.count(h[2])==4:
					score=8+0.01*h[2]+0.0001*b
			elif len(s)==3:
				if h.count(h[2])==3:
					score=4+0.01*h[2]+0.0001*list(s-set([h[2]]))[1]+0.000001*list(s-set([h[2]]))[0]
				else:
					r=(x for x in s if h.count(x)==2)
					b=r.next()
					c=r.next()
					score=3+0.01*c+0.0001*b+0.000001*list(s-set([b])-set([c]))[0]
			else:
				r=(x for x in s if h.count(x)==2)
				b=r.next()
				c=list(s-set([b]))
				score=2+0.01*b+0.0001*c[2]+0.000001*c[1]+0.00000001*c[0]
		else:
			score=1+0.01*h[4]+0.0001*h[3]+0.000001*h[2]+0.00000001*h[1]+0.0000000001*h[0]
	return score


def is_straight(nums):
	return ((nums[4]-nums[3]==1) or (nums[4]==14 and nums[0]==2)) and (nums[3]-nums[2]==1) and (nums[2]-nums[1]==1) and (nums[1]-nums[0]==1)

f=open('C:/Users/Phil/Programming/Project Euler/Labview/Text Files/poker.txt', 'r')
e=f.read().split('\n')
e=e[:-1]
print "Answer:", sum(1 for x in e if (score_hand(x[:14])>score_hand(x[15:])))



elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")