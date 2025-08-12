m,n=(map(int,input().split()))
ans=int(0)
if m%2==0:
    ans=(m//2)*n
    print(ans)
else:
    ans=((m-1)//2)*n
    if n%2==0:
        ans2=n//2
        result=int(ans+ans2)
        print(result)
    else:
        ans2=(n-1)//2
        result = ans + ans2
        print(result)


