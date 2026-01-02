n=int(input())

for i in range(n):
    m = int(input())
    l=list(map(int,input().split()))
    s=set(l)
    k=list(s)
    x=len(l)
    a=int(0)
    b=int(0)
    ans1=int(0)
    ans2=int(0)
    for j in range(x):
        if l[j]==k[0]:
            a=a+1
            ans1=j
        else:
            b=b+1
            ans2=j
    if a>1:
        print(ans2+1)
    else:
        print(ans1+1)
