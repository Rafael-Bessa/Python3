print("****************************")
print()

n = int(input("Quantas linhas? >>> "))
p = [1]

for i in range(1,n+1):
    print(p)
    p.append(0)
    w = [1]
    for j in range(len(p)):
        if j>0:
            w.append(p[j-1]+p[j])
    p = w



