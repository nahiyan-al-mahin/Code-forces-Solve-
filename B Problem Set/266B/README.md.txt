# Codeforces Problem 266B -Queue at the School

**Problem Link:** https://codeforces.com/problemset/problem/266/B

## Problem Description

There is a line in canteen and there are boys and girls.
If a boy has girl behind him he lets that girl move in front of him
and only one girl at a time. This happens same time in that whole line
we have to calculate for each time how the line will look


## Solution Approach

We take input of students number and time then we take students input inside a list.
Then inside for loop its for the time and then while loop for students number
if a student is boy and the next one is girl we just swap them and if we swap them
we move the value of k by 2 as they swapped if not k value moves normally
last we print how we want our output  


## Code

n,t=map(int,input().split())
students=list(input().strip())
for i in range(t):
    k=0
    while k < n-1:
        if students[k]=="B" and students[k+1]=="G":
            students[k],students[k+1]="G","B"
            k+=2
        else:
            k+=1
print(''.join(students))