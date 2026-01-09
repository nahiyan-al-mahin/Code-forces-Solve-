# Codeforces Problem 469A -I Wanna Be the Guy

**Problem Link:** https://codeforces.com/problemset/problem/469/A

## Problem Description

There are a total number of levels in a game and two players. If they cooperate with each other they can pass all levels. We have to find if they can.




## Solution Approach

We first take input of how many levels then we take input of first player total level passed number alongside with what levels that player passed. We then take the same input for second player.
Then we pop the first index from both list. Because that number is not any level number but its how many level they passed. Then we turn that list into set to remove all duplicates.
Lastly we check if the length of set is equal to the total number of level given in first.
If it is we print "I become the guy."
If it is not we print "Oh, my keyboard!"

## Code

n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
l.pop(0)
m.pop(0)
ans=list(l)+list(m)
ans=set(ans)
if (len(ans) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
