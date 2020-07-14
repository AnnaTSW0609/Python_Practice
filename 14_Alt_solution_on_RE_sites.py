# Solution from https://github.com/jssssv007/stackexcahnge/blob/master/thebillionyearwar.py

def reverse(l):
	t=""
	for i in range(len(l)):
		if(l[i]=='A'):
			t=t+'T'
		elif(l[i]=='T'):
			t=t+'A'
		elif(l[i]=='C'):
			t=t+'G'
		elif(l[i]=='G'):
			t=t+'C'
	return t
    
def rev(d):
	return d[len(d)::-1]

p=input()

for i in range(len(p)):
	for j in range(4,14):
		if (p[i:i+j]==rev(reverse(p[i:i+j]))and i+j<=len(p)):
			print(i+1, end=" ")
			print(j)
# PS this worked
# Why 
