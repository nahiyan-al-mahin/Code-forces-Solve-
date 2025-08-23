# Codeforces Problem 148A -Insomnia cure

**Problem Link:** https://codeforces.com/problemset/problem/148/A

## Problem Description

There are dragons index numbers and we have to find these numbers from the total dragon numbers to find how many dragons suffered moral or physical damage.


## Solution Approach

First we take inputs of all type of damage numbers and total dragon number.
Then we create an empty list and inside loop that will run until all the dragon number is checked,
we check and store how many numbers are divisible by these damage numbers.
After loop we use set to remove all duplicates and then then length of that set list is our ans.


## Code

k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
ans=[]
for i in range(1,d+1):
    if i%k==0:
        ans.append(i)
    if i%l==0:
        ans.append(i)
    if i%m==0:
        ans.append(i)
    if i%n==0:
        ans.append(i)
real=set(ans)
x=len(real)
print(x)