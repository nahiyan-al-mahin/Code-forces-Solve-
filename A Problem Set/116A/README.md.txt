# Codeforces Problem 116A -Tram

**Problem Link:** https://codeforces.com/problemset/problem/116/A

## Problem Description

There is a tram and we have to find its minimum possible capacity. Every i-th stop some passengers exit and some enter.
Tram starts with 0 and finishes with 0. 



## Solution Approach

We first take input of the stops tram will make then we go inside for loop and we take input of
exit and entered passengers. We calculate to know how much passengers inside the tram and then we keep the max number
inside a variable. We print that variable


## Code

n=int(input())
m=int(0)
z=int(0)
for i in range(n):
    a,b=map(int,input().split())
    m=(m-a)+b
    z=max(m,z)

print(z)