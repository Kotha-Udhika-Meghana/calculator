n=int(input("enter a value"))
l=[]
while(n>0):
    l=l+[n%10]
    n=n//10
l.reverse()
print(l)