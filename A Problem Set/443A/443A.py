x=list(input().split())
y=x[0]
z=x[-1]
m=x[1:-1]
y=y[1:]
z=z[:-1]
z=z[0]+","
m.append(z)
m.append(y)
p=len(m)
found=int(0)
for i in range(p):
    if m[i]=="{" :
        found=1
    if m[i]=="}":
        found = 1
    if m[i] == "{,":
        found = 1
    if m[i]=="},":
        found = 1
if found==1 and m[0]!="{" and m[1]!="}":
    ans=set(m)
    print(len(ans)-1)
elif found==1:
    print("0")
elif found>=2:
    print("0")
elif found==0:
    ans = set(m)
    print(len(ans))

