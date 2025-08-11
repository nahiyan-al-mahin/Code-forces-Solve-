n,h=map(int,input().split())
ans=int(0)
p=list(map(int,input().split()))

for pl in p:
    if pl>h:
        ans=ans+2
    else:
        ans=ans+1

print(ans)









