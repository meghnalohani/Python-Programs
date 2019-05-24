t=int(input())
for i in range(t):
    flag=True
    a=input()
    b=input()
    c=input()
    w1=list(a)
    w2=list(b)
    w1.reverse()
    w2.reverse()
    
    for ch in c:
        if len(w1)!=0 and ch==w1[-1]:
            w1.pop()
            
        elif len(w2)!=0 and ch==w2[-1]:
            w2.pop()
            
        else:
            flag=False
            break
    if(flag==True):
        print("true")
    else:print("false")
    
            
