# Codeforces Problem 110A -Nearly Lucky Number

**Problem Link:** https://codeforces.com/problemset/problem/110/A

## Problem Description

If a number has 4 or 7 they are lucky. Only if they are 4 times or 7 times in that digit. It does not matter if only 4 or 7 is there which matters is they have to be there
4 or 7 times and that digit is lucky


## Solution Approach

First take input of user in a string. Then we take one variable which will store the number of
4 or 7 in that string. We take length size of string and run our loop for the whole string.
inside loop it will be if as if number is 4 m will increment by 1 or number is 7 m will increment by 1.
Then outside loop if m==4 or m==7 means digit is lucky if not that is unlucky.


## Code

y=input()
m=int(0)
length=len(y)
for i in range(length):
    if y[i]=='4' or y[i]=='7':
        m=m+1

if(m==4 or m==7):
    print("YES")
else:
    print("NO")
