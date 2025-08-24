# Codeforces Problem 443A -Anton and Letters

**Problem Link:** https://codeforces.com/contest/443/problem/A

## Problem Description

There is some English letter inside parenthesis.
We need to find how many English letter is there without duplicate.


## Solution Approach

We first take input of all letters inside parenthesis.
Then we exclude the parenthesis from front and back and then add the letters on list.
Then we set this list so all duplicates will be removed.
Then we check if still parenthesis was inserted into the list as if there was only one letter
parenthesis will insert the list.
If found value is one and the first member is not parenthesis then we just print the number minus one.
Because we add "," in all letters.
If found value is one only then we found parenthesis only and we print zero.
If found value is more then 2 then we found parenthesis and we print zero.
If found value is zero we print ans(length of list)  


## Code

x=list(input().split())
y=x[0]
z=x[-1]
m=x[1:-1]
y=y[1:]
z=z[:-1]
z=z[0]+","
m.append(z)
m.append(y)
p=len(m)
found=int(0)
for i in range(p):
    if m[i]=="{" :
        found=1
    if m[i]=="}":
        found = 1
    if m[i] == "{,":
        found = 1
    if m[i]=="},":
        found = 1
if found==1 and m[0]!="{" and m[1]!="}":
    ans=set(m)
    print(len(ans)-1)
elif found==1:
    print("0")
elif found>=2:
    print("0")
elif found==0:
    ans = set(m)
    print(len(ans))
