n = int(input("Até qual número: >>> "))

print(f"\033[1:32mTodos os pares positivos até o {n}\033[m")
print('0')
for i in range(1, n+1):
    if i*2 < n+1:
        print(i*2)
print("~"*30)
print("~"*30)
print(f"\033[1:31mTodos os ímpares positivos até {n}\033[m")
for j in range(1, n+1, 2):
    print(j)




