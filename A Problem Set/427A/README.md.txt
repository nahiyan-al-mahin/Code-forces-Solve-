# Codeforces Problem 427A -Police Recruits

**Problem Link:** https://codeforces.com/problemset/problem/427/A

## Problem Description

There is a police station and they are hiring. One police can attend one crime at a time.
If there is no police that crime will happen. We have to find out how many crimes will happen.


## Solution Approach

We first take input of the total numbers of input.
Then we take input of the crimes and new hirings in a list.
We declare two variables and then we run a loop.
Inside loop if a hiring happened we will update police value.
Then if the number is -1 means a crime happened we go to else and see if any police is available.
If not we increase the crime. If available then we minus the police value.
Last we print the crime numbers


## Code

n=int(input())
l=list(map(int,input().split()))
crm=int(0)
police=int(0)
for i in range(n):
    if l[i]>0:
        police+=l[i]
    else:
        if police>0:
            police-=1
        else:
            crm+=1
print(crm)
