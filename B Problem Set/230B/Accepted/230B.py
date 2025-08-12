import math
limit = 10**6 + 1
prime = [True] * limit
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(limit)) + 1):
    if prime[i]:
        for j in range(i * i, limit, i):
            prime[j] = False

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    root = int(math.sqrt(num))
    if root * root == num and prime[root]:
        print("YES")
    else:
        print("NO")
