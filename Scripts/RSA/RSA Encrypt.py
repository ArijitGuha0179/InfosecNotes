choice=int(input("1. n is given\n2. p and q are given\nEnter choice: "))
if choice==1:
	n=int(input("Enter n: "))
else:
	p=int(input("Enter p: "))
	q=int(input("Enter q: "))
	n=p*q
	print("n:",n)
e=int(input("Enter e: "))
m=int(input("Enter plaintext m: "))
c=(m**e)%n
c=1
while e!=0:
	if e%2==1:
		c=((c%n)*(m%n))%n
	m=((m%n)*(m%n))%n
	e=e//2
print("Ciphertext c:",c)
