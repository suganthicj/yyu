x11,x=map(int,input().split())
l=list(map(int,input().split()))
z11=0
for o in range(0,len(l)-1):
	for t in range(o+1,len(l)):
		if l[o]+l[t]==x:
			z11=z11+1
if z11>0:
	print("yes")
else:
	print("no")
