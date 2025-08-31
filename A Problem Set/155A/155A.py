n=int(input())
l=list(map(int,input().split()))
s=len(l)
ma=l[0]
ans=int(0)
p= [l[0]]
for i in range(s):
    q=max(p)
    o=min(p)
    p.append(l[i])
    x=max(p)
    y=min(p)
    if q!=x:
        ans+=1
    elif o!=y:
        ans+=1

print(ans)

