n=int(input())
m=int(0)
z=int(0)
for i in range(n):
    a,b=map(int,input().split())
    m=(m-a)+b
    z=max(m,z)

print(z)













