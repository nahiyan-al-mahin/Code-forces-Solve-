# Codeforces Problem 228A -Is your horseshoe on the other hoof?

**Problem Link:** https://codeforces.com/problemset/problem/228/A

## Problem Description

There are 4 horseshoe.We have to find how many needs to change so there wont be any duplicates. 


## Solution Approach

First we take input inside list.
Using set we remove all duplicates and find its length.
We find real list length also.
Last we minus real list length with new set list length.
That is our ans.


## Code

num=list(map(int,input().split()))
x=len(set(num))
y=len(num)
ans=y-x
print(ans)