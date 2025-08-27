# Codeforces Problem 141A -Amusing Joke

**Problem Link:** https://codeforces.com/problemset/problem/141/A

## Problem Description

There are 3 files total. First line is guest name, second is the residence host.
Third is the pile of all letters that were found.
We have to check if all letters were found or any extra letter is there.


## Solution Approach

First we take inputs of all three lines in three separate lists.
Then we marge the first two list(name and host).
Then we take third list input and we sort both sum of line one and two list and third input of the list.
Then we check if both are same or not.


## Code

n=list(map(str,input()))
l=list(map(str,input()))
p=list(map(str,input()))
m=n+l
m.sort()
p.sort()
if p==m:
    print("YES")
else:
    print("NO")