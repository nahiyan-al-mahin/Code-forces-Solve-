# Codeforces Problem 271A -Beautiful Year

**Problem Link:** https://codeforces.com/problemset/problem/271/A

## Problem Description

We have to find if a year has no duplicate numbers
Such as 1987,2013,2014
and not 1988,2012,2011



## Solution Approach

We first take input of year and then convert it to int to increment as
we have to find the next year. Then we again convert it to a string.
Then we take a variable year_found as true to run while loop until we find our year.
inside while loop we check if every index is same with one another if not we convert
the year into int and increment one then again convert it to string for checking.
If we found our year we change our true to false and exit from loop and print that year.


## Code

year1=input()
year1=int(year1)+1
year1=str(year1)
year_found=True
while year_found:
    if year1[0]==year1[1] or year1[0]==year1[2] or year1[0]==year1[3] :
        year1=int(year1)+1
        year1=str(year1)
    elif year1[1]==year1[2] or year1[1]==year1[3]:
        year1=int(year1)+1
        year1=str(year1)
    elif year1[2]==year1[3] :
        year1=int(year1)+1
        year1=str(year1)
    else:
        year_found=False
print(year1)
