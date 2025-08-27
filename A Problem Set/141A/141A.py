n=list(map(str,input()))
l=list(map(str,input()))
p=list(map(str,input()))
m=n+l
m.sort()
p.sort()
if p==m:
    print("YES")
else:
    print("NO")
