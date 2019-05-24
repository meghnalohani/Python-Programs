n=int(input())
f=0
a=[]
for i in range(n):
    a.append(input())
    
for i in range(n):
    
    p=a[i]
    a1=p[6]
    a2=p[7]
    d1=int(p[11:])
    d2=int(p[9:11])
    as1=ord(a1)
    as2=ord(a2)
    if as1-as2==d1-d2:
        print ("Not Fake")
    else:
        print ("Fake")
        f+=1
if f==0:
    print ("We Are Safe")
else:
    if f==1:
        print ("Fake Taxi Spotted")
    else:
        print ("Fake Taxis Spotted")
