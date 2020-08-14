l=[3,2,1,4]
s=0
c=len(l)
for i in l:
    s=s+i*(10**(c-1))
    c=c-1
print(s)