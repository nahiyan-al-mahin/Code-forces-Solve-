# Codeforces Problem 1676A -Lucky?

**Problem Link:** https://codeforces.com/contest/1676/problem/A

## Problem Description

A number is given we have to find out if first three numbers sum is equal to last three numbers sum.



## Solution Approach

We first take input of how many numbers we will take input.
Then we take input of our numbers inside loop as integers.
Inside loop we just access the index number of first three and last three numbers and sum them.
Then we check if they are equal. 


## Code

n=int(input())
for i in range(n):
    m=list(map(int,input()))
    sum1=m[0]+m[1]+m[2]
    sum2=m[3]+m[4]+m[5]
    if sum1==sum2:
        print("YES")
    else:
        print("NO")