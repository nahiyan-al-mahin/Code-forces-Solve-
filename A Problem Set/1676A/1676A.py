n=int(input())
for i in range(n):
    m=list(map(int,input()))
    sum1=m[0]+m[1]+m[2]
    sum2=m[3]+m[4]+m[5]
    if sum1==sum2:
        print("YES")
    else:
        print("NO")