# Codeforces Problem 1899A -Game with Integers

**Problem Link:** https://codeforces.com/problemset/problem/1899/A

## Problem Description

Two friends are playing a game to see if one can take their number and make it divisible by 3.



## Solution Approach

We first take input of how many numbers we will take input.
Then we take input of our number inside loop as integers.
Then we check if our number is divisible by 3. If it is Vova will win as she can go round and round to stop making Vanya win. But if the remaining is 1 or 2 that means Vanya can win before 10 rounds as all they have to do is add 1 or subtract 1.


## Code

n=int(input())
for i in range(n):
    m=int(input())
    if m%3==0:
        print("Second")
    else:
        print("First")
