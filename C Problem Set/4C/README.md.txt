# Codeforces Problem 4C -Registration system

**Problem Link:** https://codeforces.com/problemset/problem/4/C

## Problem Description

There is a registration system and we have to take user names as input.
If one name matches we have to add numbers in the last based on how many same names are there.


## Solution Approach

We take input of how many users.
We take a empty dictionary and then go inside loop
Then we take one input at a time.
if name already matches then we add number in the last
if don't we just print ok



## Code

n=int(input())

c={}
for i in range(n):
    name = input().strip()
    if name in c:
        c[name]+=1
        print(name + str(c[name] - 1))
    else:
        c[name] = 1
        print("OK")

