# Codeforces Problem 344A -Magnets

**Problem Link:** https://codeforces.com/problemset/problem/344/A

## Problem Description

There is a domino of magnates and positive and negative side are represented as 0 and 1.
If its positive and positive next to each other they will connect.
We have to find how many groups are there like
01 01 01 is a group and 10 10 10 is another




## Solution Approach

We first take input of how many magnets are there and make an empty list.
Inside loop we take input of the magnets and add them inside the list.
We then take a new empty list to store groups and a new variable to track the members that will be stored inside groups list.
Inside second loop we check if neighbor are same to same. If they are same we increment member.
If they are not same we add member number in the groups list and then set member to 1 again.
Outside loop we append the last member number in group and then we find how many elements inside groups list.
We print the ans.  


## Code

n=int(input())
mags=[]
for i in range(n):
    mag=input().split()
    mags.append(mag)
groups=[]
mem=int(1)
for i in range(n-1):
    if mags[i]==mags[i+1]:
        mem+=1
    else:
        groups.append(mem)
        mem=1
groups.append(mem)
ans=len(groups)
print(ans)
