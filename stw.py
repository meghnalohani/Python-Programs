import time
start_time = time.time()
def gossipypeople(a):
    count=0
    for i in a:
        if i==1:
            count+=1
    return count
t=int(input())
output=[]
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=[0]*n
    flag[0]=1
    days=0
    i=0
    c=arr[0]
    while(flag[n-1]==0 and i<n):
        i=0
        c=gossipypeople(flag)
        while(i<c):
            tellppl=arr[i]
            told=0
            j=0
            while(told<tellppl and j<n):
                if flag[j]==0:
                    flag[j]=1
                    told+=1
                j+=1
            
            i+=1
        days+=1
    output.append(days)    
for i in output:
    print (i)
print("--- %s seconds ---" % (time.time() - start_time))
                    
                
    
        
                    
                
                
                
                
                

        
    
    
        
