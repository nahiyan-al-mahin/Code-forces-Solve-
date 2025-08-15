year1=input()
year1=int(year1)+1
year1=str(year1)
year_found=True
while year_found:
    if year1[0]==year1[1] or year1[0]==year1[2] or year1[0]==year1[3] :
        year1=int(year1)+1
        year1=str(year1)
    elif year1[1]==year1[2] or year1[1]==year1[3]:
        year1=int(year1)+1
        year1=str(year1)
    elif year1[2]==year1[3] :
        year1=int(year1)+1
        year1=str(year1)
    else:
        year_found=False
print(year1)