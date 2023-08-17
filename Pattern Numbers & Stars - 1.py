n=int(input())
nst=n;
nsp=-1;
val=1;
for i in range(0,n):
	for j in range(0,nst):
		print(val,end=" ")
		val=val+1;
	for k in range(0,nsp):
		print("*",end=" ")
	nst=nst-1
	nsp=nsp+2
	val=1
	print()
