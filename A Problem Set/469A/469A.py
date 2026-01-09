n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
l.pop(0)
m.pop(0)
ans=list(l)+list(m)
ans=set(ans)
if (len(ans) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")