# Codeforces Problem 230B -T-primes

**Problem Link:** https://codeforces.com/contest/230/problem/B

## Problem Description

If a number has exactly three positive divisor then its T-Prime. We have to find numbers that have exactly three divisor. 


## Solution Approach

We have to first set a limit and set everything as prime number
then we set 0,1 as not prime. WE run a loop according to Sieve Algorithm.
Loop will continue till limit. If we find any number that is not prime we make it false.
The main formula and clue of this code is
we have to check if number is perfect square and that square root it prime.
so T-prime= prime square 

## Code

import math
limit = 10**6 + 1
prime = [True] * limit
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(limit)) + 1):
    if prime[i]:
        for j in range(i * i, limit, i):
            prime[j] = False

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    root = int(math.sqrt(num))
    if root * root == num and prime[root]:
        print("YES")
    else:
        print("NO")
