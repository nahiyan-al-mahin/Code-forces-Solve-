# Codeforces Problem 136A -Presents

**Problem Link:** https://codeforces.com/problemset/problem/136/A

## Problem Description

Petya have n friends and at New Year party they exchange gifts. Petya wants to know which friends gifts which one.
I'th friend gifts what number is on that i'th place friend.


## Solution Approach

Frist we take input of how many friends.
Then we take input of who gave gifts to whom.
Then we turned that list values into integers.
We find the length of that list.
We then create a empty list same size as friends list.
Inside loop we just place members on that index value list.
As friends starts with 1 we adjusted the index numbering.



## Code

n=int(input())
friends=input().split()
newf=list(map(int,friends))
x=len(newf)
ans=[0]*x
for i in range(x):
    ans[newf[i]-1]=i+1
print(*ans)
