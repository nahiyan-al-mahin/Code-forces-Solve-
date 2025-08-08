# Codeforces Problem 158A -Next Round

**Problem Link:** https://codeforces.com/contest/158/problem/A

## Problem Description

There are contestant and we will set a point limit. If one fails to obtain that point they will not go to next round. Point will be set from contestant points. 


## Solution Approach

first we have to take input of contestant and whose point will be the limit that number
then we can take input directly in a list as we want to store that inside an array
then we will set a limit 
and there will be a count to calculate how many user will go to next round
inside for loop we will simply check if point is bigger or equal then limit and also if point is 0
then we will increment 
last we print


## Code

import math
n, m, a =map(int,input().split())
result=(math.ceil(n/a)*math.ceil(m/a))
print(result) 

n,k=(map(int,input().split()))
points = list(map(int, input().split()))

limit = points[k - 1]
count = 0

for point in points:
    if point >= limit and point > 0:
        count += 1

print(count)