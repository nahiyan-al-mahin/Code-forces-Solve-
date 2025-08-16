# Codeforces Problem 1A -Watermelon

**Problem Link:** https://codeforces.com/contest/4/problem/A

## Problem Description

There is a watermelon and two friends. They want to have even number of divided watermelon. 
We have to calculate the even number they can have. 


## Solution Approach

If the number is divided by 2 and is large then 2 then they can have equal even number watermelon.


## Code

n=int(input())
if n%2==0 and n>2:
    print("YES")
else:
    print("NO")
