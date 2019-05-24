t=int(input())
flag=True
if t>100:
    exit()
output=[]
for i in range(t):
    ttime=0
    left=set(['d','f'])
    right=set(['j','k'])
    words=[]
    timearray=[]
    nw=int(input())
    if nw>100:
        exit()
    
    
    for i in range(nw):
        wrd=input()
        if len(wrd)>20:
            exit()
        
        if wrd in words:
            pos=words.index(wrd)
            tx=timearray[pos]/2
            
            timearray.append(tx)
            continue 

        time=0.2
        for i in range(1,len(wrd)):
            ch=wrd[i]
            cx=wrd[i-1]
            if (ch not in left and ch not in right) or (cx not in left and cx not in right):
                exit()
            elif ch in left and cx in left:
                time=time+0.4
            elif ch in right and cx in right:
                time=time+0.4
            else:
                time=time+0.2
    
        
        words.append(wrd)
        timearray.append(time*10)
    
    s=0
    for i in timearray:
        s=s+i
    s=round(s)
    output.append(s)

for i in output:
    print(i)
    
                
    
