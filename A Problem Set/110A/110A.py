y=input()
m=int(0)
length=len(y)
for i in range(length):
    if y[i]=='4' or y[i]=='7':
        m=m+1

if(m==4 or m==7):
    print("YES")
else:
    print("NO")






