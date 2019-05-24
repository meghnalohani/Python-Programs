n=int(input())
output=[]
for i in range(n):
    a=list(map(int,input().split()))
    c=a[0]
    pos=a[1]
    arr=list(map(int,input().split()))
    arr2=arr.sort(reverse=True)
    score=arr[pos-1]
    count=0
    for i in range(c):
        if arr[i]>=score:
            count=count+1
    output.append(count)
for i in range(n):
    print(output[i])
    
