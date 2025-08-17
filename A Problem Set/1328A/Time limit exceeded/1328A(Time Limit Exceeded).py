n=int(input())
for i in range(n):
    ans = int(0)
    a=list(map(int,input().split()))
    if a[0]%a[1]==0:
        print(ans)
    else:
        found=True
        while found:
            if a[0]%a[1]==0:
                print(ans)
                found=False
            else:
                ans+=1
                a[0]+=1


















