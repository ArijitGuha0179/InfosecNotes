choice=int(input("1. n is given\n2. p and q are given\n3. any one of p and q are given\nEnter choice: "))
if choice==1:
	n=int(input("Enter n: "))
	tot=n
elif choice==3:
	n=int(input("Enter n: "))
	p=int(input("Enter p: "))
	q=n//p
	print("q:",q)
	tot=(p-1)*(q-1)
else:
	p=int(input("Enter p: "))
	q=int(input("Enter q: "))
	n=p*q
	print("n:",n)
	tot=(p-1)*(q-1)
print("Totient:",tot)
e=int(input("Enter e: "))
d=65537
c=int(input("Enter ciphertext c: "))
m=1
while d!=0:
	if d%2==1:
		m=((m%n)*(c%n))%n
	c=((c%n)*(c%n))%n
	d=d//2
print("Plaintext m:",m)