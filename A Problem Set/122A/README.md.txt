# Codeforces Problem 122A -Lucky Division

**Problem Link:** https://codeforces.com/problemset/problem/122/A

## Problem Description

A number is lucky if it can be divided by 4,7 or divisible by numbers containing both of them(like 44,47,77,74).
It is also lucky if it has only 4 or 7 or both.



## Solution Approach

We first take input of the number and take it as string.
Find the length and run loops. We check first if all index number is 4 or 7.
If its 4 or 7 we increment number tracker variable(we created it before).
If the number does not have 4 or 7 that means we have to check if its divisible by any of that number.
We check divisibility by 4,7,44,77,74,47 and if it is then we print and break.
If not we print another output.
and in the last we check if all numbers were 4,7.
If that was true then we print output.


## Code

n=input()
x=len(n)
word=int(0)
for i in range(x):
    if n[i]=='4' or n[i]=='7':
        word=word+1
    else:
        num=int(n)
        if num%4==0 or num%7==0 or num%44==0 or num%77==0 or num%74==0 or num%47==0:
            print("YES")
            break
        else:
            print("NO")
            break
if word==x:
    print("YES")