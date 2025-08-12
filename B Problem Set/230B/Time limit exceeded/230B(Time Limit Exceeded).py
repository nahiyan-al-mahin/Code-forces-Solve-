import math
n=int(input())
num=list(map(int,input().split()))
m=len(num)
for i in range(m):
    if num[i]<4:
        print("NO")
    else:
        x=0
        z=int(math.sqrt(num[i]))
        if z*z==num[i]:
            #q=int(math.sqrt(z))
            for k in range(2,z):
                if z%k==0:
                    x=x+1
                    break
            if x==0:
              print("YES")
            else:
                print("NO")
        else:
            print("NO")
















