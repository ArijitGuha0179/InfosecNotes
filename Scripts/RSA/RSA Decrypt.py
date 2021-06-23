choice=int(input("1.n is given\n2.p and q are given\n3.any one of p and q are given\n4.: n and totient is given\nEnter choice: "))
if choice==1:
	n=int(input("Enter n: "))
	for i in range(2,n):
		if n%i==0:
			p=i
			break
	q=n//p
	print("p:",p)
	print("q:",q)
	tot=(p-1)*(q-1)
	print("Totient:",tot)
elif choice==3:
	n=int(input("Enter n: "))
	p=int(input("Enter p: "))
	q=n//p
	print("q:",q)
	tot=(p-1)*(q-1)
	print("Totient:",tot)
elif choice==2:
	p=int(input("Enter p: "))
	q=int(input("Enter q: "))
	n=p*q
	print("n:",n)
	tot=(p-1)*(q-1)
	print("Totient:",tot)
elif choice==4:
	n=int(input("Enter n: "))
	tot=int(input("Enter totient: "))
e=int(input("Enter e: "))
'''
i=1
while True:
	if(((tot*i)+1)%e==0):
		d=((tot*i)+1)//e
		break
	i+=1
print("d:",d)
'''
d=pow(e,-1,tot)
print("d: ",d)
c=int(input("Enter ciphertext c: "))
m=1
while d!=0:
	if d%2==1:
		m=((m%n)*(c%n))%n
	c=((c%n)*(c%n))%n
	d=d//2
print("Plaintext m:",m)

