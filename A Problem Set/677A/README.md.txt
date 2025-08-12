# Codeforces Problem 677A -Vanya and Fence

**Problem Link:** https://codeforces.com/problemset/problem/677/A

## Problem Description

There is a fence of height h and Vanya and his friends have to go without noticing by guard.
If any friend is taller then fence then they have to bend and take double space. They want to walk in a single row



## Solution Approach

We first take input of number of people and fence height in a map then we declare a variable which will count
what is the width. Then we take friends height input in a list. Inside for loop we just check the list member.
If they are bigger then h(height) then we plus 2 as they have to bend and take double space and if they are 
inside height then we just plus 1 as they would take normal space. Last we print the ans. 


## Code

n,h=map(int,input().split())
ans=int(0)
p=list(map(int,input().split()))

for pl in p:
    if pl>h:
        ans=ans+2
    else:
        ans=ans+1

print(ans)