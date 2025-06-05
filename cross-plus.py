n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("x ",end=" ")
        else:
            print("  ",end=" ")
    print()
    
n=int(input("enter no..(try odd number)"))
print("even also works")
x=n-1

m=x//2

for i in range(m):
    print("  "*m+"x "+"  "*m)
print(n*"x ")
for i in range(m):
    print("  "*m+"x "+"  "*m)
    
