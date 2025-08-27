n,k,l,c,d,p,nl,np=map(int,input().split())
tl=k*l
ans1=tl//nl
lm=c*d
sl=p//np
ans=min(ans1,lm,sl)//n
print(ans)



