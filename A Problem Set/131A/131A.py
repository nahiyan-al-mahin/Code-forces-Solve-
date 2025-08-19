n=input()
p=list(n)
x=len(p)
ans=int(0)
if p[0]>='A' and p[0]<='Z':
    for i in range(x):
        if p[i]>='A' and p[i]<='Z':
            ans+=1
    if ans==x:
        for i in range(x):
            p[i]=p[i].lower()
        print(''.join(p))
    else:
        print(''.join(p))
else:
    for i in range(x):
        if p[i]>='A' and p[i]<='Z':
            ans+=1
    if ans == x-1:
        p[0]=p[0].upper()
        for i in range(1,x):
            p[i]=p[i].lower()
        print(''.join(p))
    else:
        print(''.join(p))
































