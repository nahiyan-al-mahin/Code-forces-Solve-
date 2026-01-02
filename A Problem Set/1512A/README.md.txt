# Codeforces Problem 1512A -Spy Detected!

**Problem Link:** https://codeforces.com/problemset/problem/1512/A

## Problem Description

A same number of list is given. We have to find what number is different in the group.


## Solution Approach

We first take input of how many test case we will input.
Then we take input of our numbers inside loop as integers and store the numbers inside a list.
We turn that list into a set to identify two numbers.
We then turn that set into list again because set cannot accessed by index.
We then check inside a for loop by comparing the two numbers with the main list of numbers and keep track.
Also we store the index value inside one variable.
Then we check if one number is there more then 1 times. If its there only 1 time its our number and we print its index value. We add additional 1 because index number starts from 0.



## Code

n=int(input())

for i in range(n):
    m = int(input())
    l=list(map(int,input().split()))
    s=set(l)
    k=list(s)
    x=len(l)
    a=int(0)
    b=int(0)
    ans1=int(0)
    ans2=int(0)
    for j in range(x):
        if l[j]==k[0]:
            a=a+1
            ans1=j
        else:
            b=b+1
            ans2=j
    if a>1:
        print(ans2+1)
    else:
        print(ans1+1)
