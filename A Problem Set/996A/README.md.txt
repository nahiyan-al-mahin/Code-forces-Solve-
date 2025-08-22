# Codeforces Problem 996A -Hit the Lottery

**Problem Link:** https://codeforces.com/problemset/problem/996/A

## Problem Description

From bank we can only take 1,5,10,20,100 Dollar bills.
We have to find what is the minimum dollar bills we have to take out.



## Solution Approach

We first take input of number. We then store our numbers in another variable while
checking the number divisibility by 100. Then we change the number to the remainder.
We keep doing this for all the bills mentioned.
Last we get our ans. 


## Code

n=int(input())
ans=int(0)
ans=ans+(n//100)
n=n%100
ans=ans+(n//20)
n=n%20
ans=ans+(n//10)
n=n%10
ans=ans+(n//5)
n=n%5
ans=ans+(n//1)
n=n%1
print(ans)