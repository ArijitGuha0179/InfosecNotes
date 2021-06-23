def nth_root(x,n):
	upper_bound=1
	while upper_bound**n <= x:
		upper_bound*=2
	lower_bound=upper_bound//2
	while lower_bound<upper_bound:
		mid=(lower_bound+upper_bound)//2
		mid_nth=mid**n
		if lower_bound<mid and mid_nth<x:
			lower_bound=mid
		elif upper_bound>mid and mid_nth>x:
			upper_bound=mid
		else:
			return mid		

def nth_power(x,n):
	if n==0:
		return 1
	if n%2==0:
		return nth_power(x*x,n//2)
	return x*nth_power(x*x,(n-1)//2)
choice=int(input("1.Encrypt 2.Decrypt "))
if choice==2:
	e=int(input("Enter e: "))
	c=int(input("Enter ciphertext c: "))
	m=nth_root(c,e)
	print("Plaintext m: ",m)
else:
	e=int(input("Enter e: "))
	m=int(input("Enter plaintext m: "))
	c=nth_power(m,e)
	print("Ciphertext c: ",c)