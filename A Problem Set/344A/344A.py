n=int(input())
mags=[]
for i in range(n):
    mag=input().split()
    mags.append(mag)
groups=[]
mem=int(1)
for i in range(n-1):
    if mags[i]==mags[i+1]:
        mem+=1
    else:
        groups.append(mem)
        mem=1
groups.append(mem)
ans=len(groups)
print(ans)
