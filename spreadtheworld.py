def allpeopleKnow(flag):
    f=True
    for i in flag:
        if i==0:
            return False
        else:
            continue
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=[]
    flag=[0]*n
    flag[0]=1
    days=1
    while(not allpeopleKnow(flag)):
        for i in arr:
            ppl=i
            c=0
            pos=0
            while(c!=ppl and pos!=n):
                if flag[pos]!=1:
                    flag[pos]=1
                    pos+=1
                    c+=1
                else:
                    pos+=1
        days+=1
print (days)
                    
                
                
                
                
                

        
    
    
        
