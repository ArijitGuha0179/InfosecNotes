from sympy import solve,Symbol
n=int(input("Enter n: "))
x=int(input("Enter p-q (x): "))
p=Symbol('p')
P=solve(p**2-x*p-n,p)[1]
Q=n//P
assert P*Q==n
print("p: ",P)
print("q: ",Q)
print("")
tot=(p-1)*(q-1)
print("totient: ",tot)
e=int(input("Enter e: "))
d=pow(e,-1,tot)
print("d: ",d)
c=int(input("Etner ciphertext (c): "))
m=pow(c,d,n)
print("Original (m): ",m)