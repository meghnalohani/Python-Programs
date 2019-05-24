n=int(input())
out=[]
for i in range(n):
    a=[]
    a=list(map(int,input().split()))
    exp=a[0]
    l=a[1]
    b=a[2]
    c=a[3]
    h=list(map(int,input().split()))
    s=0
    for i in h:
        s=s+i*c
    if s>exp:
        out.append("Enough")
        
    elif s==exp:
        out.append("Just Enough")
        
    else:
        out.append("Not Enough")
       
for i in out:
    print (i)
