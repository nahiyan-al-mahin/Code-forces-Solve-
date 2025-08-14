n=input()
x=len(n)
word=int(0)
for i in range(x):
    if n[i]=='4' or n[i]=='7':
        word=word+1
    else:
        num=int(n)
        if num%4==0 or num%7==0 or num%44==0 or num%77==0 or num%74==0 or num%47==0:
            print("YES")
            break
        else:
            print("NO")
            break
if word==x:
    print("YES")















