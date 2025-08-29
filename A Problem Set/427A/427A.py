n=int(input())
l=list(map(int,input().split()))
crm=int(0)
police=int(0)
for i in range(n):
    if l[i]>0:
        police+=l[i]
    else:
        if police>0:
            police-=1
        else:
            crm+=1
print(crm)
