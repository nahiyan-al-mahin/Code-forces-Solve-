# Codeforces Problem 131A -cAPS lOCK

**Problem Link:** https://codeforces.com/problemset/problem/131/A

## Problem Description

There is a word. If the first letter is lowercase and the rest of the letter is uppercase
we need to change the rest of the letter to lowercase and the first one to uppercase.
If all are uppercase we change it to lowercase. If there are more then one lowercase and uppercase
mixed we keep it as it is.


## Solution Approach

Frist we take input of the word. We then turn it to a list.
We check if our words first letter is uppercase. If it is,
then we check if all are uppercase. We store that track inside a variable.
We then check and if all are uppercase we turn all into lowercase. If not
we print what we had.
If our first letter is lowercase we do the same thing again. 



## Code

n=input()
p=list(n)
x=len(p)
ans=int(0)
if p[0]>='A' and p[0]<='Z':
    for i in range(x):
        if p[i]>='A' and p[i]<='Z':
            ans+=1
    if ans==x:
        for i in range(x):
            p[i]=p[i].lower()
        print(''.join(p))
    else:
        print(''.join(p))
else:
    for i in range(x):
        if p[i]>='A' and p[i]<='Z':
            ans+=1
    if ans == x-1:
        p[0]=p[0].upper()
        for i in range(1,x):
            p[i]=p[i].lower()
        print(''.join(p))
    else:
        print(''.join(p))
