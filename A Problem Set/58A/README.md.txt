# Codeforces Problem 58A -Chat room

**Problem Link:** https://codeforces.com/contest/58/problem/A

## Problem Description

There is a gibberish word and i have to find out if it says "hello". Hello will only be accepted if each letter comes after one another in serial(index).

## Solution Approach

First we take input and find the length.
Then we take a variable which will count the "hello".
Then we take another variable which will check index numbers.
Inside for loop we check each word and increment variable C(takes track of hello).
We store index number in another variable.
For the rest of elif we just check if words were found in serial and says "hello".
Last just checks if words tracking variable is equal to 5(as hello has 5 words).
Then we print output.



## Code

n=input()
x=len(n)
c=int(0)
last=int(0)
for i in range(x):
    if n[i]=='h' and c==0 :
        c+=1
        last=i
    elif n[i]=='e' and c==1 and i>last:
        c+=1
        last = i
    elif n[i]=='l' and c==2 and i>last:
        c+=1
        last = i
    elif n[i]=='l' and c==3 and i>last:
        c+=1
        last = i
    elif n[i]=='o' and c==4 and i>last:
        c+=1
        last = i
if c==5:
    print("YES")
else:
    print("NO")
