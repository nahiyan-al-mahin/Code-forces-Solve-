n,k=(map(int,input().split()))
points = list(map(int, input().split()))

limit = points[k - 1]
count = 0

for point in points:
    if point >= limit and point > 0:
        count += 1

print(count)

