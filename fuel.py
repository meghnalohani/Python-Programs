t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    x=0
    m=[]
    for i in a:x=x+i
    m2=list(map(int,input().split()))
    m=sorted(m2)
    s=0
    for i in range(len(m)):
        s=s+m[i]
        if s>x:
            print (i)
            break
            
        
