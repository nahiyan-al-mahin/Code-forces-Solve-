y=int(input())
n=list(input())
x=len(n)
for i in range(x):
    n[i]=n[i].upper()
p=set(n)
f=len(p)
if f==26:
    print("YES")
else:
    print("NO")
































