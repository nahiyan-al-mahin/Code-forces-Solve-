n=input()
x=len(n)
c=int(0)
last=int(0)
for i in range(x):
    if n[i]=='h' and c==0 :
        c+=1
        last=i
    elif n[i]=='e' and c==1 and i>last:
        c+=1
        last = i
    elif n[i]=='l' and c==2 and i>last:
        c+=1
        last = i
    elif n[i]=='l' and c==3 and i>last:
        c+=1
        last = i
    elif n[i]=='o' and c==4 and i>last:
        c+=1
        last = i
if c==5:
    print("YES")
else:
    print("NO")















