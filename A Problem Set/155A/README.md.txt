# Codeforces Problem 155A -I_love_%username%

**Problem Link:** https://codeforces.com/problemset/problem/155/A

## Problem Description

There is a contest and points number of one player.
We have to find how many times low or high points were broken.

## Solution Approach

First we take inputs of how many points will be there.
Then we take the points input.
We find out the length to run loop.
We insert the first value in a new list to find out max and min later.
Inside loop we first find max and min of that new list and then append one value.
Then we find out max and min again.
If max and min were not matched then record was broken and we increment our ans and last print it.


## Code

n=int(input())
l=list(map(int,input().split()))
s=len(l)
ma=l[0]
ans=int(0)
p= [l[0]]
for i in range(s):
    q=max(p)
    o=min(p)
    p.append(l[i])
    x=max(p)
    y=min(p)
    if q!=x:
        ans+=1
    elif o!=y:
        ans+=1

print(ans)