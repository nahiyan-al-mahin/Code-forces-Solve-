n,t=map(int,input().split())
students=list(input().strip())
for i in range(t):
    k=0
    while k < n-1:
        if students[k]=="B" and students[k+1]=="G":
            students[k],students[k+1]="G","B"
            k+=2
        else:
            k+=1
print(''.join(students))
















