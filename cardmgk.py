output=[]
sumn=0
t=int(input())
if t>100:
    print("Exit 1")
    exit()
for i in range(t):
    n=int(input())
    if n<2 or n>1000:
        print("Exit 2")
        exit()
    sumn=sumn+n
    if sumn>10000:
        exit()
    arr1=list(map(int,input().split()))
    for num in arr1:
        if num<1 or num>10**9:
            exit()
    """for j in range(len(arr1)):
           if arr1[j]<1 or arr1[j]>10^9:
            print("Exit 3")
            exit()"""
    arr2=[]
    arr3=sorted(arr1)
    if arr1==arr3:
        output.append("Yes")
    else:
        large=max(arr1)
        small=min(arr1)
        posl=arr1.index(large)
        poss=arr1.index(small)
        if posl<poss:
            arr2=arr1[poss:]+arr1[0:posl+1]
        else:
            arr2=arr1[posl:]+arr1[0:posl]
        if arr3==arr2:
            output.append("Yes")
        else:
            output.append("No")
for i in output:
    print (i)
