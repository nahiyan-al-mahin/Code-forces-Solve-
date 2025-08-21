# Codeforces Problem 520A -Pangram

**Problem Link:** https://codeforces.com/problemset/problem/520/A

## Problem Description

If all English letter is present in a word then its pangram.
If its there is even one missing its not pangram.




## Solution Approach

We first take input of how many letters then we take input of that word as a list.
We calculate the list length and inside a loop we turn all letters as uppercase.
After that we create a new set loop so there are no duplicate. Then we find the length of that list.
If length is 26 that means all words are present. If not something is missing and we print out output. 


## Code

y=int(input())
n=list(input())
x=len(n)
for i in range(x):
    n[i]=n[i].upper()
p=set(n)
f=len(p)
if f==26:
    print("YES")
else:
    print("NO")
