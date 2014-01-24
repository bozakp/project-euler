import time
start = time.time()

a="75 0\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
grid=a.split('\n')
a=0
for x in grid:
	grid[a]=x.split()
	b=0
	for y in grid[a]:
		grid[a][b]=int(y)
		b=b+1
	a=a+1
a=1
while a<15:
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
for x in grid[14]:
	if x>a:
		a=x
print "Answer:", a

elapse = time.time()-start
print "Time(ms):", elapse*1000
raw_input("Press ENTER to exit.")