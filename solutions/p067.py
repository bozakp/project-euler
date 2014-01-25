import time
start = time.time()

f=open('../Labview/Text Files/triangle.txt', 'r')
grid=f.read().split('\n')
a=0
for x in grid:
	grid[a]=x.split()
	b=0
	for y in grid[a]:
		grid[a][b]=int(y)
		b=b+1
	a=a+1
a=1
while a<100:
	b=0
	while b<a+1:
		if b!=0 and b!=a:
			if grid[a-1][b-1]>grid[a-1][b]:
				grid[a][b]=grid[a][b]+grid[a-1][b-1]
			else:
				grid[a][b]=grid[a][b]+grid[a-1][b]
		elif b==0:
			grid[a][b]=grid[a][b]+grid[a-1][b]
		else:
			grid[a][b]=grid[a][b]+grid[a-1][b-1]
		b=b+1
	a=a+1
a=0
for x in grid[99]:
	if x>a:
		a=x
print "Answer:", a

elapse = time.time()-start
print "Time(ms):", elapse*1000

