# Codeforces Problem 1A -Theatre Square

**Problem Link:** https://codeforces.com/problemset/problem/1/A

## Problem Description

There is a shape n*m and i have to cover it with a*a tiles. Now if n or m can be divided by a then i don't need to do anything as i will need same number of tiles as n or m
but if it is not divided then i have to add one tile as i cant break a tile.


## Solution Approach

formula will be == n/a*m/a

## Code

import math
n, m, a =map(int,input().split())
result=(math.ceil(n/a)*math.ceil(m/a))
print(result) 
