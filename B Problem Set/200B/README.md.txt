# Codeforces Problem 200B -Drinks

**Problem Link:** https://codeforces.com/problemset/problem/200/B

## Problem Description

There is n drinks in fridge. Vasya makes orange cocktail and he took equal proportions of each of drinks and mixed them.
We have to calculate how much orange juice is left.


## Solution Approach

We take input then we take input inside list.
We sum all the elements on list
We just dived sum by total juice number and we have our ans.



## Code

n=float(input())
juice=list(map(int,input().split()))
total=float(0.0)
total=sum(juice)
ans=float(total/n)
print(ans)