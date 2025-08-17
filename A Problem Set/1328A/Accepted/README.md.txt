# Codeforces Problem 1328A -Divisibility Problem

**Problem Link:** https://codeforces.com/problemset/problem/1328/A

## Problem Description

There is two numbers and we have to find how many turns we need for number a to be divided by number b.


## Solution Approach

We take input of how many turns we will have.
Inside we take input of both numbers.
If its divisible it prints "0".
If not it follows the formula or remainder 
number b-(number a % number b)
That is the ans.


## Code

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a%b==0:
        print("0")
    else:
        ans=b-(a%b)
        print(ans)
