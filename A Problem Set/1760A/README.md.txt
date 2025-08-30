# Codeforces Problem 1760A -Medium Number

**Problem Link:** https://codeforces.com/problemset/problem/1760/A

## Problem Description

Three numbers are given. We have to find what number is not maximum and also not minimum.



## Solution Approach

We first take input of how many numbers we will take input.
Then we take input of our numbers inside loop as integers.
Inside loop we find the max and minimum numbers.
Then we check what number is in middle of minimum and maximum.


## Code

n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    x=min(a,b,c)
    y=max(a,b,c)
    if a==x and b==y:
        print(c)
    if b==x and a==y:
        print(c)
    if a==x and c==y:
        print(b)
    if c==x and a==y:
        print(b)
    if b==x and c==y:
        print(a)
    if c==x and b==y:
        print(a)
