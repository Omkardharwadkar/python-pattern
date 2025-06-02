n=3
for i in range(1,n+1):
    print(" " * (n - i), end="")
    
    for j in range(i):
        print("x", end=" ")
        
    print(" " * ((n - i) * 2 + 1), end="")

    for j in range(i):
        print("x", end=" ")
    
    print()
