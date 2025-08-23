k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
ans=[]
for i in range(1,d+1):
    if i%k==0:
        ans.append(i)
    if i%l==0:
        ans.append(i)
    if i%m==0:
        ans.append(i)
    if i%n==0:
        ans.append(i)
real=set(ans)
x=len(real)
print(x)




