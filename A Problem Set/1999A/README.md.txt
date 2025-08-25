# Codeforces Problem 1999A -A+B Again?

**Problem Link:** https://codeforces.com/problemset/problem/1999/A

## Problem Description

A number is given we have to find the both digits sum.



## Solution Approach

We first take input of how many numbers we will take input.
Then we take input of our numbers inside loop as integers.
Inside loop we just access the index number and sum them.
We print the ans.


## Code

n=int(input())
for i in range(n):
    l=list(map(int,input()))
    ans=l[0]+l[1]
    print(ans)