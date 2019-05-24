n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    ma=l[0]
    win=l[1]
    stack=[]
    for i in range(ma):
        stack.append(i+1)
    print (stack)
    flag=True
    while(len(stack)!=win):

        for i in range(len(stack)):
            pos=i+1
            if pos%2==0:
                stack[i]=0
            
        for j in range(len(stack)):
            if stack[j]==0:
                del(stack[j:j+1])
                
        print (stack)
        
