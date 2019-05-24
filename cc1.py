import timeit
n=int(input())
out=[]
for i in range(n):
    p=list(map(int,input().split()))
    x=[]
    y=[]
    flag=True
    x.append(p[0])
    y.append(p[1])
    x.append(p[2])
    y.append(p[3])
    x.append(p[4])
    y.append(p[5])
    for i in range(2):
        if x[i]!=y[i]:
            out.append("No")
            flag=False
            break
        for j in range(i+1,3):
            if x[i]==x[j] or y[i]==y[j]:
                out.append("No")
                flag=False
                break
        if flag==False:
            break
    if flag==True:
        out.append("Yes")
for i in out:
    print (i)

            
                
                
