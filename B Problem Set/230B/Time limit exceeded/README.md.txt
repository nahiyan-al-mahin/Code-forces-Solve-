# Codeforces Problem 230B -T-primes

**Problem Link:** https://codeforces.com/contest/230/problem/B

## Problem Description

If a number has exactly three positive divisor then its T-Prime. We have to find numbers that have exactly three divisor. 


## Solution Approach

This Solution is good but it falls under Time Limit exit!!!
We take inputs and run the loop till the numbers are checked.
At first we exclude 1,2,3 as they will not be T-Prime.
If number is bigger then these we square root that number and check 
if that root square is really that number as sometimes float values can come.
Then we run the loop to check if its prime or not and we update x value.
If x value is 0 that is prime and if not that is not prime and if all this does not happen
then also its output will be "NO"


## Code

import math
n=int(input())
num=list(map(int,input().split()))
m=len(num)
for i in range(m):
    if num[i]<4:
        print("NO")
    else:
        x=0
        z=int(math.sqrt(num[i]))
        if z*z==num[i]:
            #q=int(math.sqrt(z))
            for k in range(2,z):
                if z%k==0:
                    x=x+1
                    break
            if x==0:
              print("YES")
            else:
                print("NO")
        else:
            print("NO")
