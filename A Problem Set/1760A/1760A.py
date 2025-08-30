n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    x=min(a,b,c)
    y=max(a,b,c)
    if a==x and b==y:
        print(c)
    if b==x and a==y:
        print(c)
    if a==x and c==y:
        print(b)
    if c==x and a==y:
        print(b)
    if b==x and c==y:
        print(a)
    if c==x and b==y:
        print(a)







