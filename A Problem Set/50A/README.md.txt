# Codeforces Problem 50A -Domino piling

**Problem Link:** https://codeforces.com/problemset/problem/50/A

## Problem Description

There is a rectangular board of M*N and i have to fit 2*1 squares domino as much as possible( no overlap, cover two squares, lies inside the board)

## Solution Approach

First takes the input of M and N. Then we check if M is divisible by 2(Because if its divisible by 2 that means my 2*1 domino can fit without leaving any blank spaces). As a domino size is 2*1 i am comparing that with 2=M and 1=N. So if its divisible by 2 that means for M will be perfectly full and as we also have N so if we then multiply (M/2)*N 
we will get how many domino will fit in M. This same approach goes for N as we can rotate the domino to see maximum fit of dominos. 


## Code

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