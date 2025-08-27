# Codeforces Problem 151A -Soft Drinking

**Problem Link:** https://codeforces.com/problemset/problem/151/A

## Problem Description

There is some friends and they have k bottles of soft drinks and these bottles have l milliliters of drink.
They have c limes and they cut them into d slices. They have p grams of salt.
To make a toast they need nl milliliters drinks a slice of lime and np gram salt.
We have to find out minimum amount of toast each friend can make.

## Solution Approach

First we take inputs of all friends, bottles, drink, lime and salt.
Then we found total milliliter by multiplying bottles with drinks.
Then we divide to know how many toast was possible.
Then we found how many limes were there.
Then how many salt are there.
We find the minimum value and divide it by firends number.
That is our ans.


## Code

n,k,l,c,d,p,nl,np=map(int,input().split())
tl=k*l
ans1=tl//nl
lm=c*d
sl=p//np
ans=min(ans1,lm,sl)//n
print(ans)
