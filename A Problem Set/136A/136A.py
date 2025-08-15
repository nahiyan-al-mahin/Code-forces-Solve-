n=int(input())
friends=input().split()
newf=list(map(int,friends))
x=len(newf)
ans=[0]*x
for i in range(x):
    ans[newf[i]-1]=i+1
print(*ans)








