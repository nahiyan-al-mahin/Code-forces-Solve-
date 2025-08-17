# Codeforces Problem 1328A -Divisibility Problem

**Problem Link:** https://codeforces.com/problemset/problem/1328/A

## Problem Description

There is two numbers and we have to find how many turns we need for number a to be divided by number b.


## Solution Approach

This Solution is good but it falls under Time Limit exit!!!
We take inputs and run the loop till the numbers are checked.
At first there is a ans variable where turns will store.
Then we take input in list after that we check if both are divisible or not.
If not we run a while loop and inside we increase number a by 1 each time.
If its divisible then it exits the loop and print the ans.


## Code

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

