n=int(input())

c={}
for i in range(n):
    name = input().strip()
    if name in c:
        c[name]+=1
        print(name + str(c[name] - 1))
    else:
        c[name] = 1
        print("OK")









