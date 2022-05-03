print("*************************")

n = int(input("Qual número? >>> "))
j = 0
m = 1

for i in range (1,n+1):
    for j in range(1,i+1):
        print(m,end=" ")
        m += 1
    print()




